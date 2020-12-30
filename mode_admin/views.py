from . import admin
from flask import session

@admin.route('/')
def index():
    return "Welcome to admin webpage"

@admin.route('/login/')
def login():
    session['name'] = 'Mansour'
    print(session.get('name'))
    session.clear()
    print(session)
    return "login page"



