#!/usr/bin/env python3
from PIL import Image
import numpy as np

def chcolor(img_path: str, color: list[int, int, int]):
    img = np.array(Image.open(img_path))

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if any(img[x, y]):
                img[x, y][:3] = color

    Image.fromarray(img).save(img_path)

def hex2rgb(string: str) -> list[int, int, int]:
    src = string.removeprefix('#')
    dst = []
    for i in range(0, 6, 2):
        dst.append(int(src[i:i+2], 16))
    return dst

from pathlib import Path

for img in Path().glob("*.png"):
    chcolor(img.name, hex2rgb("#fbf1c7"))
