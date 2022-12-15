import logging
import pymysql


def get_excute():
    with open("./init.sql", "r") as sql:
        sqls = "".join(sql.readlines()).split("\n\n")
        sql_book = sqls[0]
        sql_card = sqls[1]
        sql_borrow = sqls[2]
    return sql_book, sql_card, sql_borrow


def init():
    print("\nStart initialize Database")
    # get user and pw from config
    with open("config.txt","r") as config:
        user=config.readline().split(":")[1].strip(" \n")
        pw=config.readline().split(":")[1].strip(" \n")

    try:
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user=user,
            password=pw,
            database='library',
            charset='utf8'
        )

    except Exception as e:
        logging.exception(e)

    cursor = conn.cursor()
    sql_book, sql_card, sql_borrow = get_excute()
    # excute create database
    try:
        data = cursor.execute("create database library;")
    
    except pymysql.err.ProgrammingError as p:
        print("Database 'library' already exists")
        pass
    
    cursor.execute("use library")

    # excute create table book
    try:
        t1 = cursor.execute(sql_book)
    except pymysql.err.OperationalError as o:
        print("Table 'book' already exists")
        pass

    # excute create table card
    try:
        t2 = cursor.execute(sql_card)
    except pymysql.err.OperationalError as o:
        print("Table 'card' already exists")
        pass

    # excute create table borrow
    try:
        t3 = cursor.execute(sql_borrow)
    except pymysql.err.OperationalError as o:
        print("Table 'borrow' already exists")
        pass


    conn.commit()

    cursor.close()
    print("Databse initialize finished\n")


if __name__ == "__main__":
    init()
 