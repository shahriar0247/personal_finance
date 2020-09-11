from flask import Flask, render_template
import sqlite3
import os
import sys


if getattr(sys, 'frozen', False): 

    template_folder = os.path.join(sys._MEIPASS, 'templates') 
    static_folder = os.path.join(sys._MEIPASS, 'static') 

    print(template_folder) 
    print(static_folder) 

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder) 

else: 

    app = Flask(__name__)
app.config['SECRET_KEY'] = 'salkdfjkwaelrjmvsadsadsad'

from app import database

conn, cursor = database.create_db()
database.create_table(conn, cursor)


from app import main_view
from app import exp_view
from app import income_view
from app import category_view
from app import tags_view
from app import accounts_view