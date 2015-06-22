# -*- coding: utf-8 -*-
import re
import os
import shutil
import time
import json

dir = "/Users/will/Downloads/"
filepath = "zh.json"

def rename():
    if os.path.isdir(dir):
            print ("Directory exists!")
    else:
            print ("Directory not exist.")
            time.sleep(5)
            exit()
    filelist=[]

    filelist=os.listdir(dir)
    file_object = open(filepath)
    array = []
    try:
        jsonstr = file_object.read()
        array = json.loads(jsonstr)
    finally:
        file_object.close()


    for i in filelist:
        for item in array:
            link = item['link'].encode('utf-8')
            name = item['name'].encode('utf-8') + ".mp4"
            if i in link:
                os.rename(dir + i, dir + name) #重命名



if __name__ == "__main__":
    rename();