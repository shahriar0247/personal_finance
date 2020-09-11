from app import app
from flask import render_template
import random
import sqlite3
from app.functions import *


def random_num():
    return random.randint(1, 200)


@app.route( "/" )
def main():
    random_number_for_css = random_num()
    all_balance, all_bank_balance, all_credit_balance, all_cash_balance = get_all_balance()

    print(all_balance)
    return render_template( "main/main.html" , random_number_for_css=random_number_for_css, all_balance=all_balance, all_bank_balance= all_bank_balance, all_credit_balance=all_credit_balance, all_cash_balance=all_cash_balance)

@app.route("/expexpen")
def returnback():
    return main()

@app.route("/expincome")
def returnback2():
    return main()
    