import pymysql
import tkinter as tk 
import logging
import random
import argparse

from utils.common import *


def parse_args():
    parser = argparse.ArgumentParser(description="pymysql ques6 dot 2")

    parser.add_argument("--host", default='localhost',
                        help="User host")
    parser.add_argument("--user", default='root',
                        help="User name")
    parser.add_argument("--password", default='Zmz020513',
                        help="User password")
    parser.add_argument("--port", default=3306,
                        help="Connection port")
    parser.add_argument("--dbname", default='finance',
                        help="User database")

    return parser.parse_args()


def StartGui():
    init_win = tk.Tk()  
    # basedesk(root)
    root = MY_GUI(init_win)
    root.set_init_window()
    init_win.mainloop()


if __name__ == "__main__":
    args = parse_args()
    StartGui()