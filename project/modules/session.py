#!/usr/bin/env python3
# coding=utf-8

from flask import Flask, session, redirect, url_for, request, escape
app = Flask(__name__)

app.secret_key = 'any random string'
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"登录的用户名是:{username}<p><a href = './logout'>点击这里注销</a></p>"
    return "你还没有登录<p><a href = './login'>点击这里登录</a></p>"

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return  redirect(url_for('index'))
    return """

    <form action="#" method="POST" >
        <p><input type="text" name="username"/></p>
        <p><input type="submit" value = '登录'/></p>
     </form>

       """
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == '__main__':                                      
    app.run(debug=True,host='0.0.0.0') 

