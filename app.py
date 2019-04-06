#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:20:23 2019

@author: krunal
"""
from flask import Flask, render_template, flash, request, redirect
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

dropzone = Dropzone(app)
# Dropzone settings

app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'video/*'
app.config['DROPZONE_PARALLEL_UPLOADS'] = 1
app.config['DROPZONE_MAX_FILE_SIZE'] = 35

# Uploads settings
app.config['UPLOADED_VIDEO_DEST'] = os.getcwd()+"\\videos"


@app.route("/", methods=['GET', 'POST'])
def index():
    '''
    rendering main screen,
    it will take video as input and edit it
    '''
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_VIDEO_DEST'], filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9000, debug=True)
