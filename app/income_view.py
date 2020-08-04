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

    with sqlite3.connect( "database.db" ) as conn:
        all_categories = conn.cursor().execute("select * from categories").fetchall()
        all_tags = conn.cursor().execute("select * from tags").fetchall()
        all_accounts = conn.cursor().execute("select * from accounts").fetchall()

    random_number_for_css = random_num()    
    length_of_tags=len(all_tags)
    length_of_categories=len(all_categories)
    length_of_accounts=len(all_accounts)
    print(all_tags)
    return render_template( "income/add.html" , random_number_for_css=random_number_for_css, all_categories=all_categories, length_of_categories=length_of_categories, all_tags=all_tags, length_of_tags=length_of_tags, all_accounts=all_accounts, length_of_accounts=length_of_accounts)


@app.route( "/viewincome" )
def view_income():
    with sqlite3.connect( "database.db" ) as conn:
        all_income = conn.cursor().execute("select * from income").fetchall()
        
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


