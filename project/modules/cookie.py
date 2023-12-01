#!/usr/bin/env python3
# coding=utf-8

from flask import Flask,request, render_template, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
   
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
   
    return resp

@app.route('/getcookie')
def getcookie():
    print(request.cookies)
    name = request.cookies.get('userID')
    return '<h1>welcome '+ name +'</h1>'

@app.route('/logout')
def logout():
    resp = make_response("delete test")
    resp.delete_cookie("userID")
    return resp
    

if __name__ == '__main__':                                      
    app.run(debug=True,host='0.0.0.0') 

