__author__ = 'naveen'


import os
from flask import Flask, redirect, render_template, send_file, url_for, request, flash, session, abort

app = Flask(__name__)

@app.route('/')
def index():
    # return "Welcome to pin labs :)"
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(32)
    app.run('0.0.0.0', 5000,debug=True)