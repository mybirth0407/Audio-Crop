#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Yedarm Seong
Python Version: 3.6.1
"""

# python3 -m pip install pydub

from pydub import AudioSegment

def audio_crop(start, end, old_file, new_file, fmt='wav'):
    try:
        wav_file = AudioSegment.from_file(old_file)
        crop_file = wav_file[start:end]
        crop_file.export(new_file, format=fmt)
        print('success! ' + old_file)
    except Exception as e:
        print('error! ' + old_file)

# start, end is ms unit
audio_crop(0, 1000, 'fTbTQXqo8Lc.wav', 'split_fTbTQXqo8Lc.wav')