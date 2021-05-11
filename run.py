from application import app

if __name__ == '__main__' :
    app.run(debug=True)

#
# #
#
# class User( UserMixin):
#
#     def __init__(self, password, email):
#         self.password = password
#         self.email = email
#
#     def select_user(self, email):
#         cursor = mydb.cursor()
#         cursor.execute('SELECT * FROM clients WHERE email="{}"'.format(email))
#         user = cursor.fetchone()
#         if user:
#             id = user[0]
#             print('got to users {}'.format(id))
#             return user[0]
#
#     def get_id(email):
#         cursor = mydb.cursor()
#         cursor.execute('SELECT client_id FROM clients WHERE email="{}"'.format(email))
#         user_id = cursor.fetchone()
#         if user_id:
#             print('got to user id {}'.format(user_id))
#             return user_id
#     def get_name(email):
#         cursor = mydb.cursor()
#         cursor.execute('SELECT name_first, name_last FROM clients WHERE email="{}"'.format(email))
#         name = cursor.fetchone()
#         if name:
#             print('got to name {}'.format(name))
#             return name
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     print('gothere')
#     return User.get_id(user_id)
#
#
# def query(select, frm, where):
#     cursor=mydb.cursor()
#     query=f'SELECT {select} FROM {frm} WHERE {where}'
#     cursor.execute(query)
#     result=cursor.fetchone()
#     print('query' f'{query}')
#     print(result)
#     return result
#
# def usercheck(username, email):
#     statement= 'unique_user'
#     args= (username, email, 0)
#     cursor = mydb.cursor()
#     result= cursor.callproc(statement, args )
#     cursor.close()
#     output = result[2]
#     if output == None:
#         return None
#     else:
#         return (1)
#
#
# def usercreate(username, email, firstname, lastname, password):
#     args="('%s','%s','%s','%s','%s')"%(username, email, firstname, lastname, password)
#     statement= 'call add_client'
#     query= f"{statement}{args}"
#     print(args)
#     print(query)
#     cursor = mydb.cursor()
#     cursor.execute(query)
#     mydb.commit()
#     cursor.close()
#


    # # if current_user.is_authenticated:
    # #  return redirect(url_for('home'))
    # form = LoginForm()
    # title = 'Login'
    # if form.validate_on_submit():
    #     password = query('password', 'clients', f"email='{form.email.data}'")[0]
    #     user = User(query('client_id', 'clients', f"email='{form.email.data}'")[0])
    #     #user.select_user(form.email.data)
    #     #print(user.select_user(form.email.data))
    #     print(user)
    #
    #     if user is not None and bcrypt.check_password_hash(password, form.password.data):
    #         print('after if')
    #         print(user)
    #         login_user(user, remember=form.remember.data)
    #         next_page= request.args.get('next')
    #         flash("Login Sucessful!", 'success')
    #         print(user)
    #
    #
    #         return redirect (next_page) if next_page else redirect (url_for('index'))
    #     else:
    #         flash("Login Unsucessful, Please check email and password", 'danger')
    # return render_template('login.html', title=title, form=form)

# @app.route
# def logout():
#     logout_user()

if __name__ == '__main__' :
    app.run(debug=True)