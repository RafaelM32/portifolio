from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from login_validation import verify_login, create_new_account
from projects import send_projects


app = Flask(__name__)
CORS(app)

@app.route('/')
def status():
    return "api online..."

@app.route("/login", methods=["POST"])
def login():
    login = request.json
    return make_response(jsonify(verify_login(login)))

@app.route('/create_account', methods=["POST"])
def create_account():
    user_data = request.json
    return make_response(jsonify(create_new_account(user_data)))  

@app.route('/home', methods=["POST"])
def home():
    user_data = request.json
    return make_response(jsonify(send_projects(user_data)))


app.run()