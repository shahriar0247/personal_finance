from app import app
from flask import render_template
import random
import sqlite3
from app.functions import *
from app.common_views import get_expenses, set_graph, get_month_date, get_income


def random_num():
    return random.randint(1, 200)

def get_graph(all_values):
    value_dates, value_amounts = set_graph(all_values)
    value_month_dates = get_month_date(value_dates)
    return value_month_dates, value_amounts

@app.route( "/" )
def main():
    random_number_for_css = random_num()
    all_balance, all_bank_balance, all_credit_balance, all_cash_balance = get_all_balance()

    expense_month_dates, expense_amounts = get_graph(get_expenses())
    income_month_dates, income_amounts = get_graph(get_income())
    print( get_graph(get_expenses()))
    print(get_graph(get_income()))

    return render_template( "main/main.html" , random_number_for_css=random_number_for_css, all_balance=all_balance, all_bank_balance= all_bank_balance, all_credit_balance=all_credit_balance, all_cash_balance=all_cash_balance,  expense_month_dates=expense_month_dates, expense_amounts=expense_amounts, income_month_dates=income_month_dates, income_amounts=income_amounts)

@app.route("/expexpen")
def returnback():
    return main()

@app.route("/expincome")
def returnback2():
    return main()
    