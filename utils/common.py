import hashlib
import pymysql
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk 
import time

class basedesk():
    def __init__(self,master):
        
        self.root=master
        self.root.title('Easy Student DBMS')
        self.root.geometry('1000x700')
        initGUI(self.root)


class initGUI(): 
    def __init__(self,master):
        global im
        global image
        self.master=master
        self.master.config(bg='Magenta')
        self.initwin=tk.Frame(self.master,)
        self.initwin.pack()
        self.canvas = tk.Canvas(self.initwin, width = 1000, height = 700, bg = 'blue')      

        self.title=tk.Label(self.initwin,text="Easy Student DBMS",font=("微软雅黑",30))
        self.author=tk.Label(self.initwin,text="NormanZ",font=("微软雅黑",24))
        self.canvas.create_window(400,150,anchor="nw",width=300,height=70,window=self.title)
        self.canvas.create_window(400,350,anchor="nw",window=self.author)

        image=Image.open('utils/bg.png')
        im=ImageTk.PhotoImage(image)

        # Put image into Main GUI
        self.canvas.create_image(0,0,anchor='nw',image = im)
        self.canvas.pack() 


class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = tk.Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = tk.Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = tk.Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = tk.Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = tk.Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = tk.Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = tk.Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,tk.END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,tk.END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,tk.END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(tk.END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(tk.END, logmsg_in)