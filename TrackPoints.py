import os
import shutil
from tkinter import *

h = 600
w = 800
top = Tk()
top.title('Title')


class NewFrame:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, height=h, width=w)

    def create(self):
        self.frame.grid()
        self.frame.grid_propagate(0)


def start():
    path = os.getcwd()+'/houses'
    if os.path.isdir(path):
        print('house dir already exists')
    else:
        print('creating houses dir')
        os.mkdir(path)


start()

home = NewFrame(top)
home.create()


mainloop()
