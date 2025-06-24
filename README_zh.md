# Minecraft字形转换资源包

**[English](README.md) | [中文](README_zh.md)**

----

[![Update resource pack](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/update.yml/badge.svg)](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/update.yml)[![Ruff](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/ruff.yml/badge.svg)](https://github.com/SkyEye-FAST/glyph_conversion_pack/actions/workflows/ruff.yml)

此项目用于提供将各使用汉字的语言转换为不同字形的Minecraft Java版资源包。转换使用库`opencc`。

## 下载

- [**下载最新版本资源包**](https://github.com/SkyEye-FAST/glyph_conversion_pack/releases/latest/)
- [查看历史版本](https://github.com/SkyEye-FAST/glyph_conversion_pack/releases/)

## 语言

资源包目前支持5种语言：`zh_guji`、`zh_twsc`、`zh_hksc`、`lzh_simp`和`ja_kyuu`。

### 繁體中文 (中國大陸)（[`zh_guji.json`](output/zh_guji.json)）

由`zh_cn`按《古籍印刷通用字规范字形表》（GB/Z 40637-2021）转换而来。使用[forFudan/GujiCC](https://github.com/forFudan/GujiCC)的`s2g.json`配置。

### 简化字文言 (华夏)（[`lzh_simp.json`](output/lzh_simp.json)）

由`lzh`按照《通用规范汉字表》转换而来。使用`opencc`的`t2s.json`配置。

### 简体中文 (台湾)（[`zh_twsc.json`](output/zh_twsc.json)）

由`zh_tw`按《通用规范汉字表》转换而来。使用`opencc`的`tw2s.json`配置。

### 简体中文 (香港)（[`zh_hksc.json`](output/zh_hksc.json)）

由`zh_hk`按《通用规范汉字表》转换而来。使用`opencc`的`hk2s.json`配置。

### 舊字體日本語 (日本)（[`ja_kyuu.json`](output/ja_kyuu.json)）

由`ja_jp`按《常用汉字表》（JIS X 0213:2004）转换而来。使用`opencc`的`jp2t.json`配置。

## 协议

资源包在[Apache 2.0协议](LICENSE)下发布。

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

## 反馈

遇到的问题和功能建议等可以提出议题（Issue）。

欢迎创建拉取请求（Pull request）。
