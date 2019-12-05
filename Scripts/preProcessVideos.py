# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:20:29 2019

@author: himan
"""

import sys
import os
from moviepy.editor import VideoFileClip
import subprocess

session_id = '123_1_1572972352'

path = "../Sessions/" + session_id + "/session_data/subject_media/video/"
savepath = "../Sessions/" + session_id + "/session_data/subject_media/audio/"
processvideopath = "../Sessions/" + session_id + "/session_data/subject_media/processedVideos/"

try: 
    os.mkdir(processvideopath) 
except(FileExistsError): 
    pass

formt = ".webm"
filelist = os.listdir(path)
print(filelist)

for file in filelist:
    name = file.split('.')
    name = name[len(name)-1]
    mp4name = file[0:len(file)-len(name)-1]
    print('Converting...')
    subprocess.call('ffmpeg -fflags +genpts -i' + ' '+path+file + ' -r 30' + ' ' +processvideopath+mp4name+'.mp4')
    print('Done Converting...')
    #pro = subprocess.call(['ffmpeg', '-fflags','+genpts','-i',processvideopath+file,'-r','30',path+mp4name+'.mp4' ])
    #pro.wait()
    #pro.terminate()
    #pro.kill()
#import ffmpeg
#import subprocess
#python ffmpeg -i inp.webm output.mp4
#pro = subprocess.Popen(['ffmpeg', '-fflags','+genpts','-i','inp.webm','-r','30','output.mp4' ])
#st = 
#print(st)
#subprocess.call('ffmpeg -fflags'+ ' +genpts -i inp.webm -r 30 output.mp4')
#print('executing...')
#pro.wait()
#pro.terminate()
#pro.kill()
#print('done...')