#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template,session,redirect,url_for,flash

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')

