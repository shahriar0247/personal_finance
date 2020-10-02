import sqlite3
import random
from flask import render_template, request
import calendar

def random_num():
    return random.randint(1, 200)

def render_add_page(url, error):
    with sqlite3.connect( "database.db" ) as conn:
        all_categories = conn.cursor().execute("select * from categories").fetchall()
        all_tags = conn.cursor().execute("select * from tags").fetchall()
        all_accounts = conn.cursor().execute("select * from accounts").fetchall()
    random_number_for_css = random_num()    
    length_of_tags=len(all_tags)
    length_of_categories=len(all_categories)
    length_of_accounts=len(all_accounts)
    print(all_tags)
    return render_template( url , random_number_for_css=random_number_for_css, all_categories=all_categories, length_of_categories=length_of_categories, all_tags=all_tags, length_of_tags=length_of_tags, all_accounts=all_accounts, length_of_accounts=length_of_accounts, error=error)

def get_stuff(name):
    with sqlite3.connect( "database.db" ) as conn:
        if name == "category":
            all_stuff = conn.cursor().execute("select * from categories").fetchall()
        else:
            all_stuff = conn.cursor().execute("select * from "+name+"s").fetchall()
        return all_stuff

def add_stuff(name):
    random_number_for_css = random_num()
    if request.method == "POST":
       
        
        stuff_name = request.form["stuff_name"]
        stuff_des = request.form["stuff_des"]
        if name == "account":
            account_type = request.form["account_type"]
            account_balance = request.form["account_balance"]
            account_date = request.form["account_date"]
            if stuff_name == "" or account_type == "" or account_balance == "":
                error = "Name, Type and Beginning Balance is required"
                all_stuff = get_stuff(name)
                return render_template( name+"/add.html" , random_number_for_css=random_number_for_css, all_stuff=all_stuff, error=error)
        
        else:
            if stuff_name == "":
                error = "Name is required"
                all_stuff = get_stuff(name)
                return render_template( name+"/add.html" , random_number_for_css=random_number_for_css, all_stuff=all_stuff, error=error)
        
        with sqlite3.connect( "database.db" ) as conn:
            if name == "category":
                conn.cursor().execute(" insert into categories values ( ?,? )",(stuff_name , stuff_des) )
            else:
                if name == "account":
                    conn.cursor().execute(" insert into "+name+"s values ( ?,?,?,?,?)",(stuff_name , stuff_des,account_type,account_balance,account_date) )
            
                else:
                    conn.cursor().execute(" insert into "+name+"s values ( ?,? )",(stuff_name , stuff_des) )
            conn.commit()

    all_stuff = get_stuff(name)


    
    return render_template( name+"/add.html" , random_number_for_css=random_number_for_css, all_stuff=all_stuff)


def set_graph(items):
    items2 = {}
    for item in items:
        items2[item[0]] = int(items2.get(item[0], 0)) + int(item[1])
    items2 = {k: v for k, v in sorted(items2.items(), key=lambda item: item[0])}
    print(items2)
    keys = list(items2.keys())
    values = list(items2.values())
    return keys, values

def get_month_date(dates):
    month_dates = []
    for date in dates:
        date = date[5:]
        date = date.split("-")
        month_dates.append(date[1] +" " + calendar.month_name[int(date[0])][0:3])
    return month_dates

def get_expenses():
    with sqlite3.connect( "database.db" ) as conn:
        all_expenses = conn.cursor().execute("select * from expenses").fetchall()
    return all_expenses

def get_income():
    with sqlite3.connect( "database.db" ) as conn:
        all_income = conn.cursor().execute("select * from income").fetchall()
    return all_income

