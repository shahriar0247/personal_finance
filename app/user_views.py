from app import app
from flask import render_template, request
import random
from app import database
import sqlite3

def random_num():
    return random.randint(1, 200)

@app.route( "/" )
def main():
    random_number_for_css = random_num()
    return render_template( "main/main.html" , random_number_for_css=random_number_for_css)

@app.route("/addtrans" , methods=[ "POST" , "GET" ])
def add_trans():
    if request.method ==  "POST" :
        date = request.form[ "date" ]
        name = request.form[ "name" ]
        amount = request.form[ "amount" ]
        account = request.form[ "account" ]
        catagory = request.form[ "catagory" ]
        notes = request.form[ "notes" ]
        with sqlite3.connect( "database.db" ) as conn:
            conn.cursor().execute(" insert into transactions values ( ?,?,?,?,?,? )",(date ,  name , amount , account , catagory , notes) )
            conn.commit()

    random_number_for_css = random_num()    
    return render_template( "trans/add.html" , random_number_for_css=random_number_for_css)

@app.route( "/viewtrans" )
def view_trans():
    with sqlite3.connect( "database.db" ) as conn:
        all_trans = conn.cursor().execute("select * from transactions").fetchall()
        print(all_trans)
    random_number_for_css = random_num()
    return render_template( "trans/view.html" , random_number_for_css=random_number_for_css, all_trans=all_trans)

       
    