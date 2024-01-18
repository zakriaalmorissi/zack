import sqlite3

def connect():
    conn = sqlite3.connect("DataBase.db")
    curser = conn.cursor()
    curser.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,name text, price integer ,quntity integer, total integer)")
    conn.commit()
    conn.close()

def insert(name,price,quntity,total):
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(name,price,quntity,total))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="",id=""):
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE name = ? OR id = ? ",(name,id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id= ?",(id,))
    conn.commit()
    conn.close()

def update(id,name,price,quntity,total):
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET name = ?,price = ?,quntity = ?, total = ? WHERE id = ?",(name,price,quntity,total,id))
    conn.commit()
    conn.close()







connect()




