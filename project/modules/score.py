#!/usr/bin/env python3
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('score.html', marks = score)

@app.route('/result')
def result():
    dict = {'语文':50, '数学':60, '英语':70, '物理':80}
    return render_template('result.html', result = dict)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
