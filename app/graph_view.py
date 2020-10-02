from app import app
from flask import render_template
import sqlite3
import calendar
from app.common_views import set_graph, get_month_date , get_expenses



@app.route('/graph')
def graph():
    all_expenses = get_expenses()
    dates, amount = set_graph(all_expenses)
    month_dates = get_month_date(dates)
    return render_template('graph/test1.html', date=month_dates, amount=amount)