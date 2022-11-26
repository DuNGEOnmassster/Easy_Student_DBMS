import pymysql
import random
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="pymysql ques6 dot 2")

    parser.add_argument("--host", default='localhost',
                        help="User host")
    parser.add_argument("--user", default='root',
                        help="User name")
    parser.add_argument("--password", default='******',
                        help="User password")
    parser.add_argument("--port", default=3306,
                        help="Connection port")
    parser.add_argument("--dbname", default='finance',
                        help="User database")

    return parser.parse_args()