from flask import render_template, flash, redirect, url_for
from app import app
from flask import request
from app.models import Credentials
from app import db
username2='/0'

@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])

def login():
    return render_template('index.html')

@app.route('/',methods=['POST'])
@app.route('/index',methods=['POST'])
def post_login():
        if request.form['action']=='signup':
            return render_template('register.html')
        else:
            username1=request.form.get("username","<missing username>")
            password1=request.form.get("password","<missing password>")
            print(username1)
            u=Credentials.query.filter(Credentials.username==username1)
            
            for u in u:
                print(u.username)
            try:
                if u.username==username1 :
                    if u.password==password1:
                        return redirect('/login_1')
                    else:
                        return '<html><h1>login unsuccessful</h1></html>'
                else:
                        return '<html><h1>login unsuccessfuk</h1></html>'
            except :
                return '<html<p> user not found </p></html>'
            
            

                
@app.route("/register",methods=['GET'])
def register():
    return render_template('register.html')

@app.route("/register",methods=['POST'])
def post_register():
    username1=request.form.get("username","<missing username")
    password1=request.form.get("password","<missing password>")
    confirm_password1=request.form.get("confirm_password","<missing confirm_password>")
    print(password1)
    print(confirm_password1)
    if password1 == confirm_password1:
        u=Credentials(username=username1,password=password1)
        db.session.add(u)
        try:
            db.session.commit()
            status=1
        except :
            db.session.rollback()
            status=0
        return render_template('reg_status.html',status=status)
    else:
        return '<html><h1>Password not matched plaese try again! </h1> <br><br><a href="/index"> HOME</a> </html>'
@app.route('/login_1')
def login_1():
    return render_template('book.html')

            







