#!/usr/bin/env python3

from PIL import Image
import numpy as np

from chcolor import hex2rgb

img = np.full((3, 20, 4), [*hex2rgb("#8ec07c"), 0xff], dtype=np.uint8)

Image.fromarray(img).save("separator.png")
