#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 Kajetan Knopp <kajetan@knopp.com.pl>
#
# Distributed under terms of the MIT license.

"""
The main route file for the Flask web application.
"""
from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)
app.secret_key = "Code4Ukraine"

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
