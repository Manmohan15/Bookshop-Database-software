import sqlite3

def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(t,a,y,isb):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(NULL,?,?,?,?)",(t,a,y,isb)) 
    conn.commit()
    conn.close()  
def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") 
    rows=cur.fetchall() 
    conn.close()
    return rows 
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn)) 
    rows=cur.fetchall() 
    conn.close()
    return rows   
def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store where id=?",(id,)) 
    conn.commit()
    conn.close()  
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("Update store SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id)) 
    conn.commit()
    conn.close()




  


