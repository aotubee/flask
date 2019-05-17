#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template,session,redirect,url_for,flash
from flask import request,current_app
from datetime import datetime

from . import main
from . import forms
from .forms import NameForm
from .. import db
from .. import mail
from flask_mail import Mail,Message
from ..models import User

def send_email(to,subject,template,**kwargs):
    msg=Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=current_app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    mail.send(msg)

@main.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
#            user=User(username=form.name.data)
#            db.session.add(user)
            session['known']=False
#            #如果存在管理员邮箱地址
#            if current_app.config['FLASKY_ADMIN']:
#                send_email(current_app.config['FLASKY_ADMIN'],'New User','mail/new_user',user=user)
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('main.index'))
    return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False),current_time=datetime.utcnow())
