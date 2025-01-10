from flask import Flask, request, jsonify
from pymongo import MongoClient
from bcrypt import hashpw, gensalt, checkpw

app = Flask(_name_)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['user_database']
collection = db['users']

# Route for signup
@app.route('/signup', methods=['POST'])
def signup():
    username = request.json['username']
    password = request.json['password']

    # Check if username already exists
    if collection.find_one({'username': username}):
        return jsonify({"message": "Username already exists"}), 400

    # Hash the password
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    
    # Store username and hashed password in the database
    collection.insert_one({'username': username, 'password': hashed_password})
    return jsonify({"message": "User created successfully"}), 201