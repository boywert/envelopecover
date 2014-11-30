#!/usr/bin/python
#-*-coding: utf-8 -*-
import PIL
import sys
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def print_image(list,filename):
    # font = ImageFont.truetype("Arial-Bold.ttf",14)
    font = ImageFont.truetype("THSarabun.ttf",60)
    img=Image.new("RGBA",(1400,1000),(255,255,255))
    draw = ImageDraw.Draw(img)      
    y_offset = 130                  
    x_offset = 0                    
    draw.text((x_offset+190,y_offset),u"เรียนเชิญ",(0,0,0),font=font)
    print list[0]                              
    draw.text((x_offset+450,y_offset+180),unicode(list[0]+"  ","utf-8"),(0,0,0),font=font)
    #draw.text((x_offset+450,y_offset+280),unicode(list[1]+"  ","utf-8"),(0,0,0),font=font)
    #draw.text((x_offset+450,y_offset+390),unicode(list[2]+"  ","utf-8"),(0,0,0),font=font)
    img2 = img.rotate(180)                                    

    # #A4 paper
    # img_final = Image.new("RGBA",(1589,2227),(255,255,255))
    # img_final.paste(copy,(0,0))
    img2.save(filename) 

import csv
import time
import os


csvfile = open(sys.argv[1],'rb')

import hashlib
from datetime import datetime

m = hashlib.md5()
m.update(str(datetime.now()))

folder = m.hexdigest()
output = sys.argv[2]
namelist = csv.reader(csvfile)


os.system("mkdir -p "+folder)
i = 0
for name in namelist:
    print_image(name,folder+"/image_"+"%05d"%(i)+".png")
    i += 1

os.system("convert "+folder+"/*.png "+output)
os.system("rm -rf "+folder)
