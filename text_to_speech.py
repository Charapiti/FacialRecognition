from pyttsx3 import *
import cv2
import numpy as np
import os
import sys


def Speak_Error(error_message):
    speak(error_message)


try:
    dir_path = 'Images'
    entries = os.listdir(dir_path)
    file_names = [entry for entry in entries]
    images_info = []

    for i in file_names:
        images_info.append(cv2.imread('Images/' + i, 0))
    print("Done reading files")

    for i in images_info:
        cv2.imshow('image', i)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    

except Exception as e:
    Speak_Error(e)