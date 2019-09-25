import os
import shutil
from tkinter import *

h = 600
w = 800


def start():
    path = os.getcwd()+'/houses'
    if os.path.isdir(path):
        print('house dir already exists')
    else:
        print('creating houses dir')
        os.mkdir(path)


top = Tk()
top.title('Title')

start()

homeFrame = Frame(top, height=h, width=w)
homeFrame.pack()
homeFrame.pack_propagate(0)

mainloop()
