from flask import Flask,request,render_template
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),  nullable=False)
    password = db.Column(db.String(100), nullable=False)


@app.route('/',methods=['GET','POST'])
def sign():
    if request.method=='POST':
        user = request.form.get('name')
        password = request.form.get('password')
        hash = generate_password_hash(password)
        entry=Post(name=user,password=hash)
        db.session.add(entry)
        db.session.commit()

    return render_template('sigin.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('name')
        password = request.form.get('password')
        users = Post.query.all()

        for u in users:
             if u.name==user and check_password_hash(u.password,password):
                return  render_template('good.html')
    return render_template('login.html')



app.run()