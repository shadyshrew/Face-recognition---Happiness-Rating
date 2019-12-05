# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:20:29 2019

@author: himan
"""
#from extractAudio import extractAudio
import sys
import os
from moviepy.editor import VideoFileClip
import subprocess

session_id = '123_1_1572972352'

def preProcess(session_id):
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
    
    file_count = 1
    for file in filelist:
        name = file.split('.')
        name = name[len(name)-1]
        mp4name = file[0:len(file)-len(name)-1]
        print('Generating metadata for video '+str(file_count)+'...')
        subprocess.call('ffmpeg -fflags +genpts -i' + ' '+path+file + ' -r 30' + ' ' +processvideopath+mp4name+'.mp4')
        print('Done Converting...')
        file_count += 1

if __name__ == '__main__':
    preProcess(str(sys.argv[1]))

