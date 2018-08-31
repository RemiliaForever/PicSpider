#!/bin/python3

from PIL import Image
from PIL import PngImagePlugin

# 循环打开原图片
images = [
    '00000001.jpg',
    '00000002.jpg',
    '00000003.jpg',
    '00000004.jpg',
    '00000005.jpg',
    '00000006.jpg',
    '00000007.jpg',
]
bitmaps = []
for i in images:
    bitmaps.append(Image.open(i))

# 创建目标图片
sample = bitmaps[0]
width = sample.width
height = sample.height
result = Image.new('RGB', (width, height * len(bitmaps)))

print(f'Width: {width}')
print(f'Height: {height} x {len(bitmaps)}\n')

# 循环复制像素
for y in range(0, height):
    print(f'copying {y+1}/{height}', end='\r')
    for x in range(0, width):
        for i in range(0, len(bitmaps)):
            result.putpixel((x, 7 * y + i), bitmaps[i].getpixel((x, y)))

print('Finish!')
# 写入exif数据
meta = PngImagePlugin.PngInfo()
meta.add_text('Frames', str(len(bitmaps)))
# result.save('result.png',pnginfo=meta)
result.convert('P').save('result.png', pnginfo=meta)
