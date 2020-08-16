from app import app
from flask import render_template
import random
import sqlite3

def random_num():
    return random.randint(1, 200)

def get_all_balance():
    with sqlite3.connect( "database.db" ) as conn:
        all_accounts = conn.cursor().execute("select * from accounts").fetchall()
        all_balance = 0
        all_bank_balance = 0
        all_credit_balance = 0
        all_cash_balance = 0
        for a in all_accounts:
            all_balance = int(a[3]) + all_balance

            if a[2] == "Bank":
                all_bank_balance = int(a[3]) + all_bank_balance
           
            if a[2] == "Credit":
                all_credit_balance = int(a[3]) + all_credit_balance
 
            if a[2] == "Cash":
                all_cash_balance = int(a[3]) + all_cash_balance
            
        
    
    print(all_balance, all_bank_balance, all_credit_balance, all_cash_balance)
    return all_balance, all_bank_balance, all_credit_balance, all_cash_balance
           
        

@app.route( "/" )
def main():
    random_number_for_css = random_num()
    all_balance, all_bank_balance, all_credit_balance, all_cash_balance = get_all_balance()

    print(all_balance)
    return render_template( "main/main.html" , random_number_for_css=random_number_for_css, all_balance=all_balance, all_bank_balance= all_bank_balance, all_credit_balance=all_credit_balance, all_cash_balance=all_cash_balance)
