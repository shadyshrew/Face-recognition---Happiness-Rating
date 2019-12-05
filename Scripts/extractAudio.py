# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:20:29 2019

@author: himan
"""

import sys
import os
from moviepy.editor import VideoFileClip

session_id = '123_1_1572972352'
#session_id = str(sys.argv[1])

path = "../Sessions/" + session_id + "/session_data/subject_media/processedVideos/"
savepath = "../Sessions/" + session_id + "/session_data/subject_media/audio/"

try: 
    os.mkdir(savepath) 
except(FileExistsError): 
    pass

formt = ".wav"
filelist = os.listdir(path)

for file in filelist:   
    name = file.split('.')
    name = name[len(name)-1]
    mp4name = file[0:len(file)-len(name)-1]
    video = VideoFileClip(path+file)
    audio = video.audio
    audio.write_audiofile(savepath+mp4name+formt)
