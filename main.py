from flask import request, render_template, redirect, session, flash, Flask


"""Configure flask object and set database"""
app = Flask(__name__)



@app.route('/')
def show_form():
    """ Home page and shows submission form """
    messages = []
    return render_template("form.html")