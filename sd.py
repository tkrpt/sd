#!/usr/bin/env python3
from os import system
system('ffmpeg -f concat -i m -vf "scale=512:512:force_original_aspect_ratio=decrease,pad=720:720:-1:-1" sd.mp4')
