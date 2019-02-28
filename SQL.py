# encoding=utf-8
import sqlite3
def insertinfo(user,pwd,headers):
    sql='insert into phone (userid,pwd,headers) VALUES (?,?,?)'
    conn=sqlite3.connect("wifi.db")
    cursor=conn.cursor()
    cursor.execute(sql,(user,pwd,headers))
    conn.commit()
    cursor.close()
    conn.close()
