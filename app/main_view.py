from app import app
from flask import render_template
import random

def random_num():
    return random.randint(1, 200)

@app.route( "/" )
def main():
    random_number_for_css = random_num()
    return render_template( "main/main.html" , random_number_for_css=random_number_for_css)
