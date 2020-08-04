from app import app
from flask import render_template, request
import random
import sqlite3

def random_num():
    return random.randint(1, 200)

@app.route( "/addaccount", methods=[ "POST" , "GET" ] )
def add_account():
    if request.method == "POST":

        account_name = request.form["account_name"]
        account_des = request.form["account_des"]
        with sqlite3.connect( "database.db" ) as conn:
            conn.cursor().execute(" insert into accounts values ( ?,? )",(account_name , account_des) )
            conn.commit()


    with sqlite3.connect( "database.db" ) as conn:
        all_accounts = conn.cursor().execute("select * from accounts").fetchall()

    random_number_for_css = random_num()
    return render_template( "account/add.html" , random_number_for_css=random_number_for_css, all_accounts=all_accounts)