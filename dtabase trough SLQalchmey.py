
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
#IT IS USE TO CONNECT DATaBSE THROUGH MYSQL like in php you do dbcon.php file
#FOR MYSQL THE ABOVE CONNECTIVITY IS DONE BY THIS STATMENT
db = SQLAlchemy(app)
#this made a class of database

class Contacts(db.Model):
    #here contact is table of coding thunder
    " id name phone msg date email"
    #"these are the above varibles from datbase"
    #and use in downlines to get connect to datbase
    #unique that every value to be unique unique default value is false
    #nullab;le means it can be empty
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),  nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    msg = db.Column(db.String(50),  nullable=False)
    #date = db.Column(db.String(12),  nullable=False)
    email = db.Column(db.String(50), nullable=False)

entry=Contacts(name="RITIK",phone="988",msg="hero",email="kas")
db.session.add(entry)
db.session.commit()


