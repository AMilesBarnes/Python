import time
import shutil
import os

def doc_list():
    for file in os.listdir("C:\Users\Barne\Desktop\Folder A"):
        if file.endswith(".txt"):
            txt_list = os.path.join("C:\Users\Barne\Desktop\Folder A", file)
            src = ''.join([str(x) for x in os.path.join(txt_list)])
            print src 
    return src
doc_list()   



