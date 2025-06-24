# Renovation Translation Resource Pack

**[English](README.md) | [中文](README_zh.md)**

----

[![Update resource pack](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/update.yml/badge.svg)](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/update.yml)[![Ruff](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/ruff.yml/badge.svg)](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/ruff.yml)

This project is used to provide a Minecraft: Java Edition resource pack that converts various languages using Hanzi / Kanji into different glyphs. The conversion uses the library `opencc`.

## Download

- [**Download the latest version**](https://github.com/SkyEye-FAST/glyph_conversion_pack/releases/latest/)
- [View previous versions](https://github.com/SkyEye-FAST/glyph_conversion_pack/releases/)

## Language

The resource pack currently supports 5 languages: `zh_guji`, `zh_twsc`, `zh_hksc`, `lzh_simp`, and `ja_kyuu`.

### 繁體中文 (中國大陸) ([`zh_guji.json`](output/zh_guji.json))

Converted from `zh_cn` based on *Standard glyph list of generally used Chinese characters for ancient books publishing* (GB/Z 40637-2021). Uses the `s2g.json` configuration from [forFudan/GujiCC](https://github.com/forFudan/GujiCC).

### 简化字文言 (华夏) (`lzh_simp.json`)

Converted by `lzh` according to *List of Commonly Used Standard Chinese Characters*. Uses the `t2s.json` configuration of `opencc`.

### 简体中文 (台湾) (`zh_twsc.json`)

Converted by `zh_tw` according to *List of Commonly Used Standard Chinese Characters*. Uses the `tw2s.json` configuration of `opencc`.

### 简体中文 (香港) ([`zh_hksc.json`](output/zh_hksc.json))

Converted from `zh_hk` according to *List of Commonly Used Standard Chinese Characters*. Uses the `hk2s.json` configuration of `opencc`.

### 舊字體日本語 (日本) ([`ja_kyuu.json`](output/ja_kyuu.json))

Converted from `ja_jp` according to *Jōyō kanji hyō* (JIS X 0213:2004). Uses the `jp2t.json` configuration of `opencc`.

## License

The resource pack is released under the [Apache 2.0 license](LICENSE).

``` text
  Copyright 2025 SkyEye_FAST

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
```

## Feedback

Please feel free to raise issues for any problems encountered or feature suggestions.

Pull requests are welcome.
