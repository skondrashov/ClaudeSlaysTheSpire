"""Crop (and optionally upscale) a region of a screenshot for overlay inspection.

usage: python crop.py <src.png> <out.png> <x> <y> <w> <h> [scale]
Coordinates are clamped to the image bounds.
"""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
x, y, w, h = (int(a) for a in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0

im = Image.open(src)
x2, y2 = min(x + w, im.width), min(y + h, im.height)
x, y = max(0, x), max(0, y)
c = im.crop((x, y, x2, y2))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(f"{out} ({c.width}x{c.height})")
