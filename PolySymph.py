#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:47:46 2020

@author: lucaspao
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'