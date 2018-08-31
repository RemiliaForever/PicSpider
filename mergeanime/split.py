#!/bin/python3

from PIL import Image
from PIL import PngImagePlugin

source = Image.open('result.png').convert('RGB')
width = source.width
height = int(source.height / 7)
print('Width: {0}'.format(width))
print('Height: {0}\n'.format(height))
bitmaps = []
for i in range(0, 7):
    bitmaps.append(Image.new('RGB', (width, height)))

# 循环复制像素
for y in range(0, height):
    print('copying {0}/{1}'.format(y + 1, height), end='\r')
    for x in range(0, width):
        for i in range(0, 7):
            bitmaps[i].putpixel((x, y), source.getpixel((x, y * 7 + i)))

print('Finish!')
# 写入exif数据
bitmaps[0].show()
for i in bitmaps:
    i.save('{0}.png'.format(bitmaps.index(i)))
