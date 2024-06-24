import math
import sys

from PIL import Image, ImageFilter

# Ensure correct usage
if len(sys.argv) != 2:
    sys.exit("Usage: Python filter.py filename")

# Open image
image = Image.open(sys.argv[1]).convert("RGB")

#Filter image according to edge detection kernel
filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))

# Show resulting image
filtered.show() 

# open golden-gate.jpg
# python filter.py golden-gate.jpg