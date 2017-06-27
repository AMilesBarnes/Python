import shutil
import os
source = os.listdir("C:\\Users\\Barne\\Desktop\\Folder A\\")  
destination = "C:\\Users\\Barne\Desktop\\Folder B\\"
def start():
    for file in source:
        if file.endswith(".txt"):
            shutil.move(os.path.join('C:\\Users\\Barne\\Desktop\\Folder A\\', file),destination)
            print 'Moving .txt file :%s ' % (file)
            print '     To loc : %s' % (destination)


start()
