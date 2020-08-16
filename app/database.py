import sqlite3


def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor
    

def create_table(conn, cursor):
    cursor.execute("create table if not exists expenses (date text, name text, amount text, destination text, category text, notes text)")
    cursor.execute("create table if not exists income (date text, name text, amount text, destination text, category text, notes text)")
    cursor.execute("create table if not exists categories (name text, des text)")
    cursor.execute("create table if not exists tags (name text, des text)")
    cursor.execute("create table if not exists accounts (name text, des text,type text, balance text, date text)")
    
    conn.commit()
    return