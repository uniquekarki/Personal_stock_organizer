import os
from menu import title
from prettytable import from_db_cursor

def disp_current(con,cur):
    title()
    cur.execute("SELECT * FROM current")
    mytable = from_db_cursor(cur)
    print(mytable)
    _ = input("Press enter to continue...")
    os.system('clear')

def disp_history(con,cur):
    title()
    cur.execute("SELECT * FROM history")
    mytable = from_db_cursor(cur)
    print(mytable)
    _ = input("Press enter to continue...")
    os.system('clear')