# nds-cartgen

A Python script that sticks image files as cartridge labels onto Nintendo DS game cards and outputs the result as a jpg file. Designed for batch processing.

## Install
1. Make sure python3 is installed
1. `python3 -m pip install --upgrade pip`
1. `python3 -m pip install --upgrade Pillow`
1. Create subdirectories `carts` and `carts/thumbnails` in the project directory

## Use
* `$python image_processing.py <path to label images>`
* The label images should be named according to the Nintendo DS [cartridge code pattern](https://www.reddit.com/r/Gameboy/comments/bux2j3/nintendo_cartridge_codes_decoded_what_that_number/). Supported codes are listed below.

| Code | Meaning | Result |
| ----------- | ----------- | ----------- |
| `NTR-____-___` | Standard cart | Standard NDS-cart |
| `TWL-____-___` | DSi enhanced cart | Standard NDS-cart |
| `NTR-I___-___` | Infrared cart | Black/slightly red NDS-cart |
| `TWL-I___-___` | Infrared cart | Black/slightly red NDS-cart |
| `CTR-____-___` | Standard 3DS cart | Standard 3DS-cart |

---
This project is not affiliated with or endorsed by Nintendo. It is a fan project made for use with homebrew software and private collecting purposes. Any use in connection with unlicensed materials or copyright infringement is not allowed.
If you want to use my code or images in another project or commercially please contact me first.
