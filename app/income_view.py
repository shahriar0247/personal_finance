from app import app
from flask import render_template, request
import random
from app import database
import sqlite3

def random_num():
    return random.randint(1, 200)


@app.route("/addincome" , methods=[ "POST" , "GET" ])
def add_income():
    if request.method ==  "POST" :
        date = request.form[ "date" ]
        amount = request.form[ "amount" ]
        account = request.form[ "account" ]
        tags = request.form[ "tags" ]
        category = request.form[ "category" ]
        notes = request.form[ "notes" ]
        with sqlite3.connect( "database.db" ) as conn:
            conn.cursor().execute(" insert into income values ( ?,?,?,?,?,? )",(date ,  amount , account , tags , category , notes) )
            conn.commit()

    random_number_for_css = random_num()    
    return render_template( "income/add.html" , random_number_for_css=random_number_for_css)

@app.route( "/viewincome" )
def view_income():
    with sqlite3.connect( "database.db" ) as conn:
        all_income = conn.cursor().execute("select * from income").fetchall()
        print(all_income)
    random_number_for_css = random_num()
    return render_template( "income/view.html" , random_number_for_css=random_number_for_css, all_income=all_income)

@app.route( "/viewincome/<id>" )
def view_income_id(id):
    try:
        with sqlite3.connect( "database.db" ) as conn:
            all_income = conn.cursor().execute("select * from income").fetchall()
            requested_id = all_income[int(id) - 1]
            print(requested_id)
        random_number_for_css = random_num()
        return render_template( "income/view_id.html" , random_number_for_css=random_number_for_css, requested_id=requested_id)
    except:
        return "Value Error, enter number not string"


