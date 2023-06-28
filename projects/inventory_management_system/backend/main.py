from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import os
import json

# Init app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'

#configiring MYSQL databse
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/rest_try'

# Initialising db
db = SQLAlchemy(app)

logged_in = {"user":[]}

# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(100))
    shoe_colour = db.Column(db.String(100), unique=True)
    shoe_size = db.Column(db.String(200))
    shoe_type = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    qty = db.Column(db.Integer)

    def __init__(self, article, shoe_colour, shoe_size, shoe_type, gender, qty):
        self.article = article
        self.shoe_colour = shoe_colour
        self.shoe_size = shoe_size
        self.shoe_type = shoe_type
        self.gender = gender
        self.qty = qty


class Inventoryusers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/login', methods=['GET', 'POST'])
def login():
    # getting all username and passwords from database
    all_users = Inventoryusers.query.all()

    # extract username and password of each user
    user_names = ["garbage"]
    passwords = ["garbage"]
    for each_user in all_users:
        user_names.append(each_user.username)
        passwords.append(each_user.password)

    # checking request method
    if request.method == "POST":
        entered_username = request.json["username"]
        entered_password = request.json["password"]

        # checking if the entered username is available in db or not and its index
        for user in user_names:
            if entered_username == user:
                index_of_user = user_names.index(entered_username)
                break
            else:
                index_of_user = False

        # if username exist in db and password entered is correct?
        if index_of_user:
            if entered_username == user_names[index_of_user] and entered_password == passwords[index_of_user]:

                logged_in['user'] = user_names[index_of_user]
                #print(logged_in['user'])
                return jsonify({"status": 200})
            else:
                return jsonify({"status": 401})
        else:
            return jsonify({"status": 401})

    # GET request
    elif request.method == 'GET':
        # if any user is logged in?
        if 'user' in logged_in:
            # extracting username's name
            for user in user_names:
                if session['user'] == user:
                    index_of_user = user_names.index(user)
                    break
                else:
                    index_of_user = False

            # if true send logged in message
            if ('user' in logged_in) and (logged_in['user'] == user_names[index_of_user]):
                send_data = {"status": 200}
                return jsonify(send_data)
        else:
            send_data = {"status": 401}
            return jsonify(send_data)


#adding storeman
@app.route('/add_storeman', methods=['POST'])
def add_storeman():

    if ('user' in logged_in) and (logged_in['user'] == 'admin'):
        username = request.json['username']
        password = request.json['password']
        cnfrm_password = request.json['cnfrm_password']

        if password == cnfrm_password:
            new_storeman = Inventoryusers(username, password)
            db.session.add(new_storeman)
            db.session.commit()
            return jsonify({"status": 200})
        else:
            send_data = {"status": 400}
            return jsonify(send_data)
    else:
        send_data = {"status": 401}
        return jsonify(send_data)

@app.route("/logout")
def logout():
    logged_in.pop('user')
    return jsonify({"status":"logged out"})


# # Get Single Products
@app.route('/product/<article>', methods=['GET'])
def get_product(article):
    # getting all products that have same article number as user mentioned from the database
    products = Product.query.filter_by(article=article).all()

    # creating empty lists to hold all the values
    shoe_colour = []
    shoe_size = []
    shoe_type = []
    qty = []
    gender = []

    # looping as there are multiple products with same article number and appending each value to its respective list
    for each_product in products:
        shoe_colour.append(each_product.shoe_colour)
        shoe_type.append(each_product.shoe_type)
        shoe_size.append(each_product.shoe_size)
        qty.append(each_product.qty)
        gender.append(each_product.gender)

    # creating dictionary to return data
    dicts = {"shoe_colour": shoe_colour, "shoe_type": shoe_type, "shoe_size": shoe_size, "gender": gender, "qty": qty}
    return jsonify(dicts)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
