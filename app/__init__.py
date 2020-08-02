from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'salkdfjkwaelrjksadlmvsadsadsad'

from app import database

conn, cursor = database.create_db()
database.create_table(conn, cursor)


from app import user_views