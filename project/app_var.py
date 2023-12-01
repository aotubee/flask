#!/usr/bin/env python3
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return '<h1>Blog Number %d</h1>' % postID

@app.route('/rev/<float:revNO>')
def revision(revNO):
    return '<h1>Revision NUmber %f</h1>' % revNO


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
