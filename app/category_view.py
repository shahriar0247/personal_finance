from app import app
from flask import render_template, request
import random
import sqlite3

def random_num():
    return random.randint(1, 200)

@app.route( "/addcategory", methods=[ "POST" , "GET" ] )
def add_category():
    if request.method == "POST":

        category_name = request.form["category_name"]
        category_des = request.form["category_des"]
        with sqlite3.connect( "database.db" ) as conn:
            conn.cursor().execute(" insert into categories values ( ?,? )",(category_name , category_des) )
            conn.commit()


    with sqlite3.connect( "database.db" ) as conn:
        all_categories = conn.cursor().execute("select * from categories").fetchall()

    random_number_for_css = random_num()
    return render_template( "category/add.html" , random_number_for_css=random_number_for_css, all_categories=all_categories)