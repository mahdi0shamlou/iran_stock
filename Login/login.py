from flask import redirect, session

def Check_login(user, password):
    if user == 'admin' and password == 'admin':
        session['Username'] = user
        session['Password'] = password
        session['Active'] = 1
        session['Path'] = 'Home'
        session['email'] = 'Admin@gmail.com'

        return redirect('/')
    else:
        return redirect('/Login')