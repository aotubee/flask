#!/usr/bin/env python3
# coding=utf-8

'''url_for 函数用于动态构建函数的URL，该函数接受函数的名称作为第一个参数，以及一个或多个关键字参数，每个参数对应于URL的可变部分。'''

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return '<h1>Hello %s as Guest</h1>' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
