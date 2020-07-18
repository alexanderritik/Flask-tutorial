from flask import Flask,request,render_template
from flask_mysqldb import MySQL
app=Flask(__name__)
#now datbase connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='databasename'

mysql=MySQL(app)

@app.route('/',methods=['POST','GET'])
def database():
    if [request.method=='POST']:
        user=request.form.get('name')
        email=request.form.get('email')
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO user(name,email) VALUES (user,email)")
        mysql.connection.connect()
        cur.close()
        return "successs"

    #how to fetch it
    cur = mysql.connection.cursor()
    result=cur.execute("SELECT * FROM user")
    if result>0:
        userdetail=cur.fetchall()
        return render_template(".html",userdetail=userdetail)

