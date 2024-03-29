from flask import Flask, render_template, redirect, request, session, json
from flask_session.__init__ import Session
from datetime import timedelta
from Login.login import Check_login
from Assets.Assets_Traded import Get_Trade_History
from Assets.Assets_Traded import Trade_Update, Trade_Delet, Trade_History_Chart, Insert_Trade_History
from Assets.Assets_favorits import Get_favorit_trade
from Assets.Multi_chart import Get_multi_chart_one_trade, Get_multi_chart_multi_trade
from Assets.Assets_favorits import Insert_Trade_History_F, Trade_Delet_F
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)
@app.route("/")
def Home():
    try:
        if not session.get("Username"):
            return redirect("/Login")
        path = session.get('Path')
        return redirect(f"/{path}")
    except:
        return render_template("/Error/index.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/index.html'), 404
@app.errorhandler(504)
def internal_error(error):
    return render_template('504/index.html'), 504
#--------------------------------------------------------------------
########################## Login
#--------------------------------------------------------------------
@app.route("/Login", methods=["POST", "GET"])
def Login():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            path = session.get('Path')
            return redirect(f"/{path}")
    except:
        return render_template("/Error/index.html")
@app.route("/Login_check", methods=["POST", "GET"])
def Login_check():
    try:
        if request.args.get("username") is None or request.args.get("pass") is None:
            return redirect("/Login")
        else:
            user = request.args.get("username")
            password = request.args.get("pass")
            Check_login_resualt = Check_login(user, password)
            return Check_login_resualt
    except:
        return render_template("/Error/index.html")
@app.route("/logout")
def logout():
    try:
        session["Username"] = None
        return redirect("/")
    except:
        return render_template("/Error/index.html")
#--------------------------------------------------------------------
########################## End Login
#--------------------------------------------------------------------
#--------------------------------------------------------------------
########################## Home
#--------------------------------------------------------------------
@app.route("/Home", methods=["POST", "GET"])
def App_main_page():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            path = session.get('Path')
            Get_Trade_History_list = Get_Trade_History()
            Get_Favorit_Trade_History_list = Get_favorit_trade()
            return render_template("/Home/index.html", Get_Favorit_Trade_History_list=Get_Favorit_Trade_History_list, Get_Trade_History_list=Get_Trade_History_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Trade_update", methods=["POST", "GET"])
def App_Trade_update():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            Trade_Update()
            return redirect('/Home')
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Delet", methods=["POST", "GET"])
def App_Trade_delet():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            ids = request.args.get('P_ID')
            if ids is None:
                return redirect('/Home')
            else:
                Trade_Delet(ids)
                return redirect('/Home')
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Trade_charts", methods=["POST", "GET"])
def App_Trade_charts():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            ids = request.args.get('P_ID')
            if ids is None:
                return redirect('/Home')
            else:
                path = session.get('Path')
                Get_Trade_History_chart = Trade_History_Chart(ids)
                return render_template("/Trade/Chart.html", Get_Trade_History_chart=Get_Trade_History_chart, user=session.get('Username'), pathmain=path, email=session.get('email'))
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Add_New_Trade", methods=["POST", "GET"])
def App_Trade_new():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            code = request.args.get('code')
            side = request.args.get('side')
            if side is None or code is None:
                path = session.get('Path')
                return render_template("/Trade/Add_new.html", user=session.get('Username'), pathmain=path, email=session.get('email'))
            else:

                Insert_Trade_History(symbol=code, side=side)
                return redirect('/Home')
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Trade_charts_multi_favorit_on_trade", methods=["POST", "GET"])
def App_Trade_charts_multi_favorit_on_trade():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            ids = request.args.get('P_ID')
            Side = request.args.get('side')
            if ids is None or Side is None:
                return redirect('/Home')
            else:
                path = session.get('Path')
                Get_Trade_History_chart = Get_multi_chart_one_trade(ids, Side)
                return render_template("/Trade/multi_charts.html", Get_Trade_History_chart=Get_Trade_History_chart, user=session.get('Username'), pathmain=path, email=session.get('email'))
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Trade_charts_multi_trade_on_favorits", methods=["POST", "GET"])
def App_Trade_charts_multi_trade_on_favorits():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            ids = request.args.get('P_ID')
            if ids is None:
                return redirect('/Home')
            else:
                path = session.get('Path')
                Get_Trade_History_chart = Get_multi_chart_multi_trade(ids)
                print(Get_Trade_History_chart)
                return render_template("/Trade/multi_charts.html", Get_Trade_History_chart=Get_Trade_History_chart, user=session.get('Username'), pathmain=path, email=session.get('email'))
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Add_New_Trade_F", methods=["POST", "GET"])
def App_Trade_new_F():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            code = request.args.get('code')
            name = request.args.get('name')
            if code is None or name is None:
                path = session.get('Path')
                return render_template("/Trade/Add_new_F.html", user=session.get('Username'), pathmain=path, email=session.get('email'))
            else:

                Insert_Trade_History_F(code, name)
                return redirect('/Home')
    except:
        return render_template("/Error/index.html")
@app.route("/Home/Delet_F", methods=["POST", "GET"])
def App_Trade_delet_F():
    try:
        if not session.get("Username"):
            return render_template("/Login/index.html")
        else:
            ids = request.args.get('P_ID')
            if ids is None:
                return redirect('/Home')
            else:
                Trade_Delet_F(ids)
                return redirect('/Home')
    except:
        return render_template("/Error/index.html")
#--------------------------------------------------------------------
########################## End Home
#--------------------------------------------------------------------
#--------------------------------------------------------------------
########################## Assets
#--------------------------------------------------------------------

#--------------------------------------------------------------------
########################## End Assets
#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1001)