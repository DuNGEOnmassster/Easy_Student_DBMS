import pymysql
import random
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="pymysql ques6 dot 2")

    parser.add_argument("--host", default='localhost',
                        help="User host")
    parser.add_argument("--user", default='root',
                        help="User name")
    parser.add_argument("--password", default='',
                        help="User password")
    parser.add_argument("--port", default=3306,
                        help="Connection port")
    parser.add_argument("--dbname", default='finance',
                        help="User database")

    return parser.parse_args()


def get_insert_content():
    return [1,1,1,1]


def connect(args):
    conn = pymysql.connect(host=args.host, user=args.user, password=args.password, port=args.port, db=args.dbname)
    cursor = conn.cursor()

    # get insert data
    trade = get_insert_content()
    # excute insert script
    for i in range((len(trade))):
        data = cursor.execute(f"show tables;")
        print(f"Insert {i+1}: {data}")
    conn.commit()

    cursor.close()


if __name__ == "__main__":
    args = parse_args()
    connect(args)