from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import datetime
import time
import shutil
import os
from os import path
import sqlite3
conn = sqlite3.connect('click_time_stamp.db')
c = conn.cursor()


def last_time():
    c.execute('''CREATE TABLE IF NOT EXISTS time_stamp (Time TEXT)''')  
last_time()


class CopyFileApp:
    
    def __init__(self, master):
        
        
        
        self.LastRun= StringVar()
        self.label = ttk.Entry(master, textvariable = self.LastRun)
        self.label.pack()
        
        button = ttk.Button(master, text = "Click For Last Run Time:", command = self.get_last_time)
        button.pack()

        self.source= StringVar()
        self.label = ttk.Entry(master, textvariable = self.source)
        self.label.pack() 
        button = ttk.Button(master, text = "Select Source Folder", command=self.load_src )
        button.pack()

        self.destination = StringVar()
        self.label = ttk.Entry(master, textvariable= self.destination)
        self.label.pack()
        button = ttk.Button(master, text = "Select Destination Folder",command=self.load_dst )
        button.pack()

        self.FilesMoved=StringVar()
        self.label = ttk.Entry(master, textvariable = self.FilesMoved)
        self.label.pack() 
        button = ttk.Button(master, text = "Copy New Files", command = self.check_file_contents)
        button.pack()

        
    def load_src(self):
        self.src = askdirectory()
        if self.src:
            self.source.set(self.src)
    
    def load_dst(self):
        self.dst = askdirectory()
        if self.dst:
            self.destination.set(self.dst)

    def get_last_time(self):
        c.execute('SELECT * FROM time_stamp ORDER BY datetime(Time) DESC Limit 1')
        l_time = c.fetchone()
        
        if l_time:
            self.LastRun.set(l_time) 
                
    def check_file_contents(self):
        unix = time.time()
        
        t_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(unix))
        
        print(t_stamp)
        c.execute("INSERT INTO time_stamp (Time) VALUES(?)",(t_stamp,))
        conn.commit()        
        time_now = time.time()
        for file in os.listdir(self.src):
            if file.endswith(".txt"):
                src_name = os.path.join(self.src,file)
                modified_time = os.path.getmtime(src_name)
                timenow = time.time()
                elapsed_time = time_now - modified_time
                if elapsed_time < 86400:   
                    shutil.copy(src_name,self.dst)
                    self.FilesMoved.set(file)
        

c.close
conn.close
              
def main():
    
    root = Tk() 
    app = CopyFileApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()

