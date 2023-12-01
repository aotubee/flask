#!/usr/bin/env python3
# coding=utf-8
'''使用POST方法，先创建一个HTML表单login.html，可以使用nginx启动此页面。
使用POST方法将表单数据发送至URL'''

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
