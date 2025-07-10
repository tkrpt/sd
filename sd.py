#!/usr/bin/env python3
from os import system
ss=open('ss/s','r').read()
ds=open('ss/d','r').read().split('\n')
for k in range(0,len(ds)):
    system('convert ds/'+str(k)+'.jpg -resize 790x790 -bordercolor white -border 20x20 -gravity center -background black -extent 1080x1080 -gravity North -pointsize 40 -fill grey -font ../sv/kv.ttf -annotate +0+40 "'+str(k)+'"  ds/'+str(k)+'.png')
system('ffmpeg -f concat -i m sd.mp4')
