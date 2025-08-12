#!/usr/bin/env python3
from PIL import Image

img = Image.open("baba.png").convert("RGBA")
assert img.size == (24, 216)

textures = []
for i in range(9):
    sprite = []
    for y in range(24):
        line = ""
        for x in range(24):
            pixel = img.getpixel((x, i * 24 + y))
            if pixel[3] == 0:
                line += " "
            elif pixel[:3] == (0, 0, 0):
                line += "B"
            else:
                line += "W"
        sprite.append(line)
    textures.append(sprite)

for i, sprite in enumerate(textures):
    print(f"texture_{i}=(")
    for line in sprite:
        print(f'"{line}"')
    print(")\n")

print("textures=(")
for i in range(9):
    print(f"texture_{i}")
print(")")
