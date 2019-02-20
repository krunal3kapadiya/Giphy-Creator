#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:20:23 2019

@author: krunal
"""
from flask import Flask, render_template
from flask_dropzone import Dropzone
app = Flask(__name__)
dropzone = Dropzone(app)
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'video/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
app.config['DROPZONE_PARALLEL_UPLOADS'] = 1
app.config['DROPZONE_MAX_FILE_SIZE'] = 35

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = '/home/krunal/Krunal/BlooskAi/uploads'


@app.route("/", methods=['GET', 'POST'])
def index():
    '''
    rendering main screen,
    it will take video as input and edit it
    '''
    return render_template('index.html')

@app.route('/results')
def results():
    '''
    Saving the file name
    '''
    return render_template('results.html')


if __name__ == '__main__':
    app.run(port=9000, debug=True)
