#!/usr/bin/env python3
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   #return '<html><body><h1>Hello World</h1></body></html>'
   return render_template('hello.html', name = user)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
