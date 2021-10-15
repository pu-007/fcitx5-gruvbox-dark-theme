#!/usr/bin/env python3

from PIL import Image
import numpy as np

# yapf: disable
THEMES = [
    {
        "theme_name": "aqua",
        "dimmed_color": "#68976a",
        "light_color": "#8ec07c"
    },
    {
        "theme_name": "blue",
        "dimmed_color": "#458588",
        "light_color": "#83a598"
    },
    {
        "theme_name": "red",
        "dimmed_color": "#cc241d",
        "light_color": "#fb4934"
    },
    {
        "theme_name": "green",
        "dimmed_color": "#98971a",
        "light_color": "#b8bb26"
    },
    {
        "theme_name": "yellow",
        "dimmed_color": "#d79921",
        "light_color": "#fabd2f"
    },
    {
        "theme_name": "purple",
        "dimmed_color": "#b16286",
        "light_color": "#d3869b"
    },
]
# yapf: enable


def _hex2rgb(string: str) -> list[int]:
    src = string.removeprefix('#')
    dst = []
    for i in range(0, 6, 2):
        dst.append(int(src[i:i + 2], 16))
    return dst


def gentheme(theme_name, dimmed_color, light_color):
    # 生成菜单栏分割线
    separator_name = "separator-" + theme_name + ".png"
    separator = np.full((3, 20, 4), [*_hex2rgb(light_color), 0xff],
                        dtype=np.uint8)
    Image.fromarray(separator).save(separator_name)
    # 生成主题文件
    with open("./base.conf", "r", encoding="utf-8") as f:
        theme = f.read()
    theme = theme.replace("<border-color>", light_color)
    theme = theme.replace("<highlight-color>", dimmed_color)
    theme = theme.replace("<separator-image>", separator_name)
    with open("./theme-" + theme_name + ".conf", "w", encoding="utf-8") as f:
        f.write(theme)

if __name__ == "__main__":
    for theme in THEMES:
        gentheme(**theme)
