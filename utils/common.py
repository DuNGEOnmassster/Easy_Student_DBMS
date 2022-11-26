import pymysql
import tkinter as tk 
from tkinter import ttk

class basedesk():
    def __init__(self,master):
        
        self.root=master
        self.root.title('Easy Student DBMS')
        self.root.geometry('1000x700')
        
        
        initwin(self.root)

class initwin(): 
    def __init__(self,master):
        self.master=master
        self.master.config(bg='Magenta')
        self.initwin=tk.Frame(self.master,)
        self.initwin.pack()
        self.canvas = tk.Canvas(self.initwin, width = 1000, height = 700, bg = 'green')      

        self.title=tk.Label(self.initwin,text="Easy Student DBMS",font=("微软雅黑",30))
        self.author=tk.Label(self.initwin,text="NormanZ",font=("微软雅黑",24))
        self.canvas.create_window(400,150,anchor="nw",width=300,height=70,window=self.title)
        self.canvas.create_window(400,350,anchor="nw",window=self.author)