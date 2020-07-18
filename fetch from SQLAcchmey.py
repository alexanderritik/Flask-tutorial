
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

# please open local host server


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
class Post(db.Model):
    #here contact is table of coding thunder
    " id name phone msg date email"
    #"these are the above varibles from datbase"
    #and use in downlines to get connect to datbase
    #unique that every value to be unique unique default value is false
    #nullab;le means it can be empty
    id = db.Column(db.Integer, primary_key=True)
    postby = db.Column(db.String(50),  nullable=False)
    topic = db.Column(db.String(50), nullable=False)

# for fetching all information from that table
users = Contacts.query.all()
for u in users:
  print(u.id, u.name,u.phone,u.msg,"\n")

#if you know the id of that person you can retrive like this where 1 is the id which you want
king= Contacts.query.get(1)
print(king.name,king.phone)

#if you want to update a different table withh the value of different table
#it is just connection differnt table in adatbase
king= Contacts.query.get(1)
p = Post(postby=king.name,topic="HERO ho BHAi")
db.session.add(p)
db.session.commit()

#
# get all posts written by a user
u = Contacts.query.get(1)
print(u.name)
king=Post.query.all()
for k in king:
    if k.postby==u.name:
        print(f"The article is posted by {u.name} and article is {k.topic}")

#to delete all table
users = Post.query.all()
for u in users:
   db.session.delete(u)

db.session.commit()


#to delete a particluer data in table
users = Post.query.get(1)
db.session.delete(users)

db.session.commit()