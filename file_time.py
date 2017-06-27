import time
import shutil
import os
from os import path

src = os.listdir('C:\Users\Barne\Desktop\Folder A')  
dst = 'C:\Users\Barne\Desktop\Folder B'

def move_recent_files(src,dst):
    
    time_now = time.time()
    for file in src:
        if file.endswith(".txt"):
            txt_loc = os.path.join('C:\Users\Barne\Desktop\Folder A',file)
            modified_time = os.path.getmtime(txt_loc)
            timenow = time.time()
            elapsed_time = time_now - modified_time
            if elapsed_time < 86400:   
                shutil.copy(os.path.join('C:\Users\Barne\Desktop\Folder A', file),dst)
                print 'Moving .txt file :%s  ' % (file)
                print '     To loc : %s' % (dst)
move_recent_files(src,dst)

    
