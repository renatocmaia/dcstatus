from app import app
from flask import render_template, request
import socket
import yaml
import os
import sys

@app.route("/index")
@app.route("/")
def index():
        return app_external()


def app_external():
	stream = open( "app/static/data/external_data.yml", 'r')
	data = yaml.load(stream)
	for elem in data:
		for d in elem['dados']:
			print(d)
			ip = socket.gethostbyname(d ['url'])
			d['ip'] = ip
			print(d)
	return render_template("index.html", data=data)


#@app.route("/login")
#def login():
	#return render_template('login.html')
@app.route("/internal_dns")
def app_internal():
        return app_internal()

def app_internal():
	stream = open( "app/static/data/internal_data.yml", 'r')
	data = yaml.load(stream)
	for elem in data:
		for d in elem['dados']:
			print(d)
			ip = socket.gethostbyname_ex(d['cname'])
			d['ip'] = ip
			print(d)
	return render_template("internal_dns.html", data=data)
