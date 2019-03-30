# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:28:57 2019

@author: kirut
"""
#Import neccesary Libraries
import numpy as np
import time
from pydub import AudioSegment
import array



#Clear the old data file
def file_clearer(file_name):
    op=open(file_name,'w')

    op.close()

#Write datas in new_song_array.txt of songtype_1
def song_array_writer(numpy_array):
    address = "C:\Users\kirut\Documents\Machine Learning\Self\Song classifier\\"

    op = open(address+"new_song_array.txt",'a')
    array = numpy_array
    string = ','.join(str(v) for v in array)+'\n'
    print(type(string))
    op.write(string)
    op.close()

#Read datas from New_Song.txt
def read_new():
    x=[]
    address = "C:\Users\kirut\Documents\Machine Learning\Self\Song classifier\NewSong\\"
    names = open(address+"NEW_SONG.txt",'r')
    n=1
    file_clearer("C:\Users\kirut\Documents\Machine Learning\Self\Song classifier\\"+"new_song_array.txt")
    old_time = time.time()
    for line in names:
        try:
            song = AudioSegment.from_mp3(address+line.strip())
            Time = song.duration_seconds
            print(line.strip()+" Song Opened")
            song_array=[Time,song.dBFS,song.rms,song.max,song.duration_seconds]
            print("Array Created")
            Song = song.get_array_of_samples()
            Song = np.array(Song)
            print(Song.shape)
            sampling_rate = int((len(Song)/Time)*0.1)
            i=0
            temp = []
            while i<=len(Song):
                if i+sampling_rate+1<len(Song):
                    temp.append(np.average(Song[i:i+sampling_rate+1]))
                else:
                    temp.append(np.average(Song[i:]))
                i+=sampling_rate
            print(np.array(temp).shape)
            if True:
                numpy_array = song_array+temp
                print("Converted to Numpy Array")
                numpy_array = [song.frame_rate,song.sample_width,song.frame_width,song.channels]+numpy_array
                song_array_writer(numpy_array)
                print((float(n)/59)*100)
                print("Expected Time to Complete")
                print(59/(float(n))*(time.time()-old_time))
                print("Time Remaining")
                print((59-n)/(float(n))*(time.time()-old_time))
            
        except:
            print ("Missed"+line.strip())
        n+=1
old_time = time.time()
read_new()
print(str(time.time()-old_time))
print("Completed")
