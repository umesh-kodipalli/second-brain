#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:29:12 2026

@author: Steven Kinghorn
"""

from flask import Flask, render_template
import markdown
import os

app=Flask(__name__)

@app.route('/')

def index():
    
    
    file_path = os.path.join(app.root_path, "files", "Taylor.md")
    file_path = os.path.normpath(file_path)
    
    #Open and read markdown file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        #Convert md in html
        html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])
        return render_template("index.html", content=html_content)
    
    except FileNotFoundError:
        return f"Error: Could not find file at {file_path}", 404
    
    if __name__ == "__main__":
        app.run(debug=True)





'''
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>My Second Brain</h1> \
            <p>Welcome to my local web app.</p>"
'''