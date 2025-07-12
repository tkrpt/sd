#!/usr/bin/env python3
from os import system
import requests
import os.path
vk=0.5
system('rm p.mp3')
system('cat ss/s| sed "s/[;,]/ /g"| SMG=1 DVNN=1 SKNL=1 ../sv/sv 6 | ffmpeg -f f32le -r 44100 -ac 1 -i - -af "adelay='+str(vk*1000).split('.')[0]+':all=true" p.mp3')
ds=open('ss/d','r').read().split('\n')[:-1]
system('mkdir -p ds')
for k in range(0,len(ds)):
    if os.path.isfile('ds/'+str(k+1)+'.jpg'):continue
    dn=ds[k]
    system('wget -O ds/'+str(k+1)+'.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/'+requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{dn}.json").json()["entities"][dn]["claims"]["P18"][0]["mainsnak"]["datavalue"]["value"].replace(' ', '_')+'"')
def lnd(k):
    return '-gravity North -pointsize 40 -fill khaki -font ../sv/kv.ttf -annotate +0+40 "'+str(k).zfill(len(str(len(ds))))+'"'
system('convert -size 1080x1080 xc:black '+lnd(0)+' ds/0.png')
for k in range(1,len(ds)+1):
    if os.path.isfile('ds/'+str(k)+'.png'):continue
    system('convert ds/'+str(k)+'.jpg -resize 790x790 -bordercolor white -border 20x20 -gravity center -background black -extent 1080x1080 '+lnd(k)+'  ds/'+str(k)+'.png')
m=''
dk=0
import subprocess
sknl=open('sknl','r').read().split('\n')[:-1]
for k in range(0,len(ds)+1):
    if k<len(ds):nk=float(sknl[k])+vk*44100
    else:nk=(float(subprocess.run(['./kl'],stdout=subprocess.PIPE).stdout.decode('utf-8')[1:-1])+1)*44100
    m=m+'file \'ds/'+str(k)+'.png\'\nduration '+str((nk-dk)/44100)+'\n'
    dk=nk
open('m','w').write(m)
system('ffmpeg -f concat -i m -i p.mp3 -c:a copy -shortest sd.mp4')
