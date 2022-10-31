# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,request
import ibm_db

import ibm_db_dbi as db2
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rds96438;PWD=DkAjeQfQZa02HKgl;",'','')
# print(conn1)

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
	return render_template("index.html")

@app.route('/about')
# ‘/’ URL is bound with hello_world() function.
def about():
	return render_template("about.html")

@app.route('/signup',methods =["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def signup():
	if request.method == "POST":
		
		email = request.form.get("email")
		password = request.form.get("psw")
		c=f"insert INTO users(email,pword) values('{email}','{password}')"
		ibm_db.exec_immediate(conn,c)
		return render_template('index.html')
	else:
		return render_template('signup.html')

@app.route('/login')
# ‘/’ URL is bound with hello_world() function.
def login():
	return render_template("login.html")



# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
