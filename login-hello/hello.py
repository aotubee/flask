#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

from flask_mail import Mail,Message
from threading import Thread
import os


app=Flask(__name__)
manager=Manager(app)

app.config['SECRET_KEY']='secret test'
bootstrap=Bootstrap(app)
moment=Moment(app)
mail=Mail(app)

class NameForm(FlaskForm):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

#设置config字典
app.config['MAIL_SERVER']='mail.ihandy.cn'
app.config['MAIL_PORT']=25
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX']='[Flasky]'
app.config['FLASKY_MAIL_SENDER']='ghxw_idc@ihandy.cn'
app.config['FLASKY_ADMIN']=os.environ.get('FLASKY_ADMIN')

db=SQLAlchemy(app)
class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Role %r>' %self.username

#定义异步发送邮件函数：
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)
def send_email(to,subject,template,**kwargs):
    msg=Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    #调用异步函数
    thr=Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr
    #mail.send(msg)

@app.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known']=False
            #如果存在管理员邮箱地址
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'],'New User','mail/new_user',user=user)
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False),current_time=datetime.utcnow())

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
migrate=Migrate(app,db)
#manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

if __name__=='__main__':
    manager.run()
#    app.run(debug=True,host='0.0.0.0')
