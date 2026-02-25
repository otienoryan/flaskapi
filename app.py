from flask import *
import pymysql
# initialize flask application
app=Flask(__name__) 
@app.route('/api/signup',methods=['POST'])
def signup():
# request user input
    username=request.form['username']
    email=request.form['email']
    password=request.form['password']
    phone=request.form['phone']
# create connection your database
    connection=pymysql.connect(host="localhost",user="root",password="",database="tembo_sokogarden_ryan")

# CREATE A CURSOR
    cursor=connection.cursor()
# create sql statement to insert the data
    sql="insert into users(username,email,password,phone)values(%s,%s,%s,%s)"
    data=(username,email,password,phone)
# execute/run
    cursor.execute(sql,data)
# commit/save
    connection.commit()

 # response
    return jsonify({"message":"thankyou for joining"})

#sign in API
# signin route
@app.route('/api/signin',methods=['post'])
def signin():
    email=request.form['email']
    password=request.form["password"]    
    
    # create a connection
    connection=pymysql.connect(host="localhost",user='root',password="",database="tembo_sokogarden_ryan")
    # create a cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # sql statement to check if user exists
    sql='select * from users where email=%s and password=%s'
    # prepare data
    data=(email,password)

    cursor.execute(sql,data)
    # response 
    if cursor.rowcount==0:
        return jsonify({'message':'login failed'})
    else:
        user=cursor.fetchone() 
        user.pop('password',None)
        return jsonify({'message':'login sucess','user':user })





































app.run(debug=True)