import sqlite3
from datetime import date, datetime
import re
conn = sqlite3.connect('attendance.db') #creates database if not exists
c = conn.cursor()

def create_table():
    conn = sqlite3.connect('attendance.db')  # creates database if not exists
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Attendance(EmpName TEXT, date TEXT,Status TEXT DEFAULT 'Absent', Time TEXT Default NULL)")
    # c.execute('alter table attendance add time TEXT')
    conn.commit()
    c.close()
    conn.close()
def data_entry(list1):
    conn = sqlite3.connect('attendance.db')  # creates database if not exists
    c = conn.cursor()
    listnew = list1
    # sql = "INSERT INTO Attendance VALUES('123',?,?,'Present',?)"
    # we need empid, empname, date, status, time
    for key, value in listnew.items():
        name = key
        time = value
        sysdate = date.today()
        d1 = sysdate.strftime("%b-%d-%Y")
        c.execute("INSERT INTO Attendance VALUES(?,?,'Present',?)",(name,d1,time))
        conn.commit()

    c.close()
    conn.close()




