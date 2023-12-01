#!/usr/bin/env python3
# coding=utf-8

from flask_wtf import Form
from wtforms import TextField

class ContactForm(Form):
       name = TextField("Name Of Student")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
