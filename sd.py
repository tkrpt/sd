#!/usr/bin/env python3
from os import system
import requests
system('rm p.mp3 && cat ss/s| sed "s/[;,]/ /g"| SMG=1 DVNN=1 SKNL=1 ../sv/sv 6 | ffmpeg -f f32le -r 44100 -ac 1 -i - -af "adelay=1s:all=true" p.mp3')
ds=open('ss/d','r').read().split('\n')[:-1]
for k in range(0,len(ds)):
    dn=ds[k]
    system('wget -O ds/'+str(k)+'.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/'+requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{dn}.json").json()["entities"][dn]["claims"]["P18"][0]["mainsnak"]["datavalue"]["value"].replace(' ', '_')+'"')
if 0:
    for k in range(0,len(ds)):
        system('convert ds/'+str(k)+'.jpg -resize 790x790 -bordercolor white -border 20x20 -gravity center -background black -extent 1080x1080 -gravity North -pointsize 40 -fill grey -font ../sv/kv.ttf -annotate +0+40 "'+str(k)+'"  ds/'+str(k)+'.png')
if 0:system('ffmpeg -f concat -i m sd.mp4')
