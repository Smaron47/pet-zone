# Store this code in 'app.py' file
import re
from flask import Flask, render_template, request, redirect, url_for, session
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import random
import os 
import json

app = Flask(__name__)

j=os.getcwd()+"/static/img/gallery"

l=os.listdir(j)

dat=open("Pets.txt","r+")
dat=dat.read()
dat=dat[1:len(dat)-1]
print(dat)
dat=dat.replace("'","\"")
dat=json.loads(dat)
print(type(dat))

@app.route('/', methods=['get'])
def index():
	print(os.getcwd())
	if not dat:
		return render_template("index.html")
	else:
		return render_template('index.html',dat=dat)
	
@app.route('/COMMAND', methods =['GET', 'POST'])
def register():

	username = request.form['line']
	if username=='login':
		return render_template('login.html')
	else:
		return index()
@app.route('/login', methods =['GET','POST'])
def login():
	if request.form['name']=="Saif Coach" and request.form['pass']=='Saif Coach':
		return render_template('amdin.html',dat=dat)
	else:
		return render_template('login.html')

@app.route('/gallery', methods=['GET','POST'])
def LogIn():
	return render_template('about.html',l=l)
@app.route("/Sell",methods=['GET','POST'])
def sell():
	return render_template("Sell.html")
@app.route("/Pets",methods=['GET','POST'])
def Pets():
	id=request.args.get("id")
	print(id)
	print(dat)
	fk=dat[id]
	im=fk["image"]
	cat=fk['catagory']
	pric=fk["price"]
	nm=fk['name']
	des=fk["description"]
	phone=fk["phone"]
	Sell_name=fk["uploader"]

	return render_template("Pets.html",nm=nm,pric=pric,cat=cat,image=im,des=des,phone=phone,Sell_name=Sell_name)

@app.route("/upload",methods=['GET','POST'])
def upl():
	name=request.form["name"]
	des=request.form["description"]
	phn=request.form["phone"]
	email=request.form["email"]
	fi=request.files["upf"]
	cta=request.form.get("cata")
	uploader=request.form["upname"]
	price=request.form["price"]
	sr=fi.filename
	fi.save(f'{j}/{sr}')
	rea=str({f'"uploader":"{uploader}","name":"{name}","phone":"{phn}","email":"{email}","catagory":"{cta}","image":"static/img/gallery/{sr}","description":"{des}","price":"{price}"'})
	rea=rea.replace("'","")
	rea=rea.replace("'","\"")
	print(rea)
	rea=json.loads(rea)	
	
	
	updic={sr:rea}
	updic=str(updic)
	updic=updic.replace("'","\"")
	print(updic)
	print(type(updic))
	updic=json.loads(updic)
	dat.update(updic)
	print(updic)
	up=str(f"'{dat}'")
	file=open("Pets.txt","w")
	file.write(up)
	file.close()	
	return render_template("index.html",dat=dat)
@app.route("/remove", methods=["GET","POST"])
def remove():
	id=request.form["options"]
	if id:
		print(id)
		dat.pop(id)
		rm=str(f"'{dat}'")
		file=open("Pets.txt","w")
		file.write(rm)
		file.close()
		os.remove(f"{j}/{id}")
		return render_template("amdin.html",dat=dat)
	else:
		return render_template("amdin.html",dat=dat)
	#dat.pop(id)
@app.route("/admin",methods=['GET','POST'])
def admin():
	return render_template("login.html")
@app.route("/contact",methods=['GET','POST'])
def contact():
	return render_template("contact.html")
if __name__ == '__main__':
       app.run(debug=True)


