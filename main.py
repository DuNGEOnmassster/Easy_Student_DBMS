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
    root = tk.Tk()  
    basedesk(root)
    root.mainloop()


def connect(args):
    try:
        conn = pymysql.connect(host=args.host, user=args.user, password=args.password, port=args.port, db=args.dbname)
    except Exception as e:
        logging.exception(e)
    
    StartGui()
    cursor = conn.cursor()

    # Todo

    cursor.close()


if __name__ == "__main__":
    args = parse_args()
    connect(args)