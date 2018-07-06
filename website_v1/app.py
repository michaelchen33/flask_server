# -*- coding: utf-8 -*-
#!/home/michaelchen/python_env/report/bin/python

from flask import Flask, url_for, make_response, Response, request, json, send_file, render_template
from flask_cors import CORS
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def home():
	return "Hey there!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5500)
