from flask import *
# initialize your flask app
app=Flask(__name__)
# define the route
@app.route('/api/home')
def home():
 return jsonify({'message':'welcome to home api'})

@app.route('/api/services')
def services():
   return jsonify({'message':'welcome to our services api'})

# create a route for products
@app.route('/api/product')
def product():
    return jsonify({'message':'welcome product api'})
# creating a route to accept user input
@app.route('/api/calc',methods=['post'])
def calc():
   num1=request.form['num1']
   num2=request.form['num2']

   sum= int(num1)+int(num2)
   return jsonify({'answer':sum})
@app.route('/api/multiply',methods=['post'])
def multiply():
   num3=request.form['num3']
   num4=request.form['num4']

   product=int(num3)*int(num4)

   return jsonify({'answer':product})













app.run(debug=True)
