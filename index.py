#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 22:12:51 2018

@author: danielkoenigsperger
"""

from flask import Flask, render_template

import data as data

app = Flask('BikeSharingData')


outputData = data.main()


@app.route('/')
def index():
    return render_template('index.html', variable = outputData)

if __name__ == '__main__':
    app.run()