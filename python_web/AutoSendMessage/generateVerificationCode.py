# -*- coding:utf-8 -*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

width = 80
height = 20
font = ImageFont.truetype(u'C:\\Windows\\Fonts\\ahronbd.ttf',23)
image = Image.new('RGB',(width,height),(0,0,0))
draw = ImageDraw.Draw(image)
for t in range(4):
	draw.text([20*t,1],str(random.randint(0,9)),font=font,fill=(255,255,255))
image.show()