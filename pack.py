"""Script for generating glyph conversion resource pack."""

import time
import zipfile as zf
from pathlib import Path
from typing import Final

import orjson
from opencc import OpenCC

# Type aliases and constant definitions
type Ldata = dict[str, str]
P: Final[Path] = Path(__file__).resolve().parent
LANG_FILES: Final[tuple[str, ...]] = ("zh_cn", "zh_tw", "zh_hk", "lzh", "ja_jp")

# Initialize OpenCC
opencc_s2c = OpenCC(str(P / "GujiCC" / "opencc" / "s2g.json"))
opencc_t2s = OpenCC("t2s.json")
opencc_tw2s = OpenCC("tw2s.json")
opencc_hk2s = OpenCC("hk2s.json")
opencc_jp2t = OpenCC("jp2t.json")


def load_json(file: str, folder: str = "data") -> Ldata:
    """Load a JSON file.

    Args:
        file (str): The filename to load, without extension
        folder (str, optional): The folder path where the JSON file is located, default is "data"

    Returns:
        dict[str, str]: The loaded JSON content
    """
    path = P / folder / f"{file}.json"
    with path.open("rb") as f:
        return orjson.loads(f.read())


def save_to_json(
    input_data: tuple[Ldata, float],
    output_file: str,
    output_folder: str = "output",
) -> None:
    """Save the generated language file to JSON.

    Args:
        input_data (tuple[Ldata, float]): Input data
        output_file (str): Filename to save, without extension
        output_folder (str, optional): Output folder, default is "output"

    Raises:
        OSError: Failed to save file
    """
    try:
        input_dict, elapsed_time = input_data
        (P / output_folder).mkdir(exist_ok=True)
        file_path = P / output_folder / f"{output_file}.json"
        json_bytes = orjson.dumps(input_dict, option=orjson.OPT_INDENT_2 | orjson.OPT_NON_STR_KEYS)
        with open(file_path, "wb") as j:
            j.write(json_bytes)
        size = file_size(file_path)
        print(
            f'Generated language file "{output_file}.json", size {size}, '
            f"elapsed {elapsed_time:.2f} s."
        )
    except Exception as e:
        raise OSError(f"Failed to save to JSON: {str(e)}") from e


def file_size(p: Path) -> str:
    """Calculate file size and return a human-readable string.

    Args:
        p (pathlib.Path): Path object of the file to calculate

    Returns:
        str: Formatted file size string
    """
    size_in_bytes = p.stat().st_size
    size = (
        f"{round(size_in_bytes / 1048576, 2)} MB"
        if size_in_bytes > 1048576
        else f"{round(size_in_bytes / 1024, 2)} KB"
    )
    return size


# Language file data
DATA: Final[dict[str, Ldata]] = {
    lang_name: load_json(lang_name, "mc_lang/full") for lang_name in LANG_FILES
}


def generate_language_files() -> float:
    """Generate language files.

    Returns:
        float: Time taken to generate language files
    """
    start_time = time.time()

    s2g_data = {k: opencc_s2c.convert(v) for k, v in DATA["zh_cn"].items()}
    t2s_data = {k: opencc_t2s.convert(v) for k, v in DATA["lzh"].items()}
    tw2s_data = {k: opencc_tw2s.convert(v) for k, v in DATA["zh_tw"].items()}
    hk2s_data = {k: opencc_hk2s.convert(v) for k, v in DATA["zh_hk"].items()}
    jp2t_data = {k: opencc_jp2t.convert(v) for k, v in DATA["ja_jp"].items()}

    save_to_json((s2g_data, time.time() - start_time), "zh_guji")
    save_to_json((t2s_data, time.time() - start_time), "lzh_simp")
    save_to_json((tw2s_data, time.time() - start_time), "zh_twsc")
    save_to_json((hk2s_data, time.time() - start_time), "zh_hksc")
    save_to_json((jp2t_data, time.time() - start_time), "ja_kyuu")

    return time.time() - start_time


def create_resource_pack() -> tuple[str, float]:
    """Package the generated language files and necessary resources as a Minecraft resource pack.

    Returns:
        tuple[str, float]: (Resource pack size, packaging time)
    """
    start_time = time.time()
    pack_path = P / "glyph_conversion_pack.zip"

    with zf.ZipFile(pack_path, "w", compression=zf.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(P / "pack.mcmeta", arcname="pack.mcmeta")
        z.write(P / "pack.png", arcname="pack.png")
        for lang_file in P.glob("output/*.json"):
            z.write(lang_file, arcname=f"assets/minecraft/lang/{lang_file.name}")

    return file_size(pack_path), time.time() - start_time


if __name__ == "__main__":
    gen_time = generate_language_files()
    print(f"\nLanguage files generated, total time: {gen_time:.2f} s.")

    pack_size, zip_time = create_resource_pack()
    print(f"\nResource pack packaged, size: {pack_size}, packaging time: {zip_time:.2f} s.")
