from flask import redirect, session

def Check_login(user, password):
    if user == 'admin' and password == 'admin':
        session['Username'] = user
        session['Password'] = password
        session['Active'] = 1
        session['Path'] = 'Home'
        return redirect('/')
    else:
        return redirect('/Login')