#!/usr/bin/env python3
# coding=utf-8

from flask import Flask,request, render_template,make_response,redirect
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['nm']
    resp = make_response(render_template('readcookie.html'))
   #  resp = make_response("success")
   # 设置cookie的两种方法，第一种
    resp.set_cookie("Itcast1", "python1")
    # max_age设置有效期，单位秒
    resp.set_cookie("userID",user,max_age=60)
    # 操作cooker实际上设置响应头，可以直接通过设置响应头操作cookie，第二种，两者二选一
   #  resp.headers["Set-Cookie"] = "Itcast3=Python3;Expires=Sat, 18-Nov-2018 04:36:04 GMT; Max-Age=3600;"
    return resp

@app.route('/getcookie')
def getcookie():
   print(request.cookies)
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'

@app.route('/logout')
def logout():
   resp = make_response("delete test")
   resp.delete_cookie("userID")
   return resp


if __name__ == '__main__':                                      
    with app.app_context():
        app.run(debug=True,host='0.0.0.0') 

