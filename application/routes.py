#import os
import secrets
#from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
#from application.models import User
from application.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_requred




# @app.route('/newitem')
# def newitem():
#     title= 'newitem'
#     active = "nav-link active"
#     return render_template('form.html', title=title)

@app.route('/')
def index():
    title= 'Index'
    active = "nav-link active"
    cuser=current_user
    return render_template('index.html', title=title, cuser=cuser)

@app.route('/register', methods=['POST', 'GET'])
def register():

    form = RegistrationForm()
    title = 'Register'
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(usercheck(username=form.username.data, email=form.email.data))
        if usercheck(username=form.username.data, email=form.email.data) is None:
            usercreate(username=form.username.data, email=form.email.data, firstname =form.first_name.data, lastname=form.last_name.data, password = hashed_password )
            flash(f"Account created for {form.username.data}!", 'success')
            return redirect('login')
        else:
            flash("There is already an account using either the username or email you input", 'danger')
    return render_template('register.html', title=title, form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    title = 'Login'
    if form.validate_on_submit():
        user = User(form.password.data, form.email.data)
        user.select_user(form.email.data)
        print(user.select_user(form.email.data))
        print('user is None?', user == None)
        print(user)
        password = query('password', 'clients', f"email='{form.email.data}'")[0]
        if user is not None and bcrypt.check_password_hash(password, form.password.data):
            login_user(user, form.remember.data)
            print("current user self.getname '{}'".format(login_fresh()))
            flash("Login Sucessful!", 'success')
            next = request.args.get('next')
            print(next)
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        else:
            flash("Login Unsucessful, Please check email and password", 'danger')

    return render_template('login.html', form=form, title=title)
