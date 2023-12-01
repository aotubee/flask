#!/usr/bin/env python3
# coding=utf-8

from flask import Flask, render_template, request,  url_for, redirect
from werkzeug.utils import secure_filename

import os

'''
在Flask 中处理文件上传非常简单。它需要一个HTML表单，其enctype属性设置为“multipart/form-data”，将文件发布到URL。
URL处理程序从request.files[]对象中提取文件，并将其保存到所需的位置。
'''

# 定义上传文件夹的路径
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin' :
        return redirect(url_for('upload_file'))
    return redirect(url_for('index'))

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        return 'file uploaded successfully'

    else:

        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
