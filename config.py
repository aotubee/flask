#!/usr/bin/env python
# coding=utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY='secret test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
    FLASKY_MAIL_SENDER='ghxw_idc@ihandy.cn'
    FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER='mail.ihandy.cn'
    MAIL_PORT=25
    MAIL_USE_SSL=False
    MAIL_USE_TLS=False
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


config = {
        'default': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        }
