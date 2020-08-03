from app import app
from flask import render_template, request
import random
from app import database
import sqlite3

def random_num():
    return random.randint(1, 200)


@app.route("/addexpen" , methods=[ "POST" , "GET" ])
def add_expen():
    if request.method ==  "POST" :
        date = request.form[ "date" ]
        amount = request.form[ "amount" ]
        source = request.form[ "source" ]
        destination = request.form[ "destination" ]
        tags = request.form[ "tags" ]
        notes = request.form[ "notes" ]
        with sqlite3.connect( "database.db" ) as conn:
            conn.cursor().execute(" insert into expenses values ( ?,?,?,?,?,? )",(date ,  amount , source , destination , tags , notes) )
            conn.commit()

    random_number_for_css = random_num()    
    return render_template( "expen/add.html" , random_number_for_css=random_number_for_css)

@app.route( "/viewexpen" )
def view_expen():
    with sqlite3.connect( "database.db" ) as conn:
        all_expen = conn.cursor().execute("select * from expenses").fetchall()
        print(all_expen)
    random_number_for_css = random_num()
    return render_template( "expen/view.html" , random_number_for_css=random_number_for_css, all_expen=all_expen)

@app.route( "/viewexpen/<id>" )
def view_expen_id(id):
    try:
        with sqlite3.connect( "database.db" ) as conn:
            all_expen = conn.cursor().execute("select * from expenses").fetchall()
            requested_id = all_expen[int(id) - 1]
            print(requested_id)
        random_number_for_css = random_num()
        return render_template( "expen/view_id.html" , random_number_for_css=random_number_for_css, requested_id=requested_id)
    except:
        return "Value Error, enter number not string"


