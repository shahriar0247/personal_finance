from app import app
from flask import render_template, request
import random
import sqlite3
from app import common_views

@app.route( "/addcategory", methods=[ "POST" , "GET" ] )
def add_category():
    return common_views.add_stuff("category")