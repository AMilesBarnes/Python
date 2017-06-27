import time
import shutil
import os
from os import path


def move_recent_files(src,dst):
    time_now = time.time()
    
    for file in os.listdir(src):
        if file.endswith(".txt"):
            src_name = os.path.join(src,file)
            modified_time = os.path.getmtime(src_name)
            timenow = time.time()
            elapsed_time = time_now - modified_time
            if elapsed_time < 86400:   
                shutil.copy(os.path.join(src, file),dst)
                
                

