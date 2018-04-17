#-*- coding:utf-8 -*-

from flask import Flask, render_template
from flask import request, jsonify, make_response
from api import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history', methods=['GET', 'POST', 'PUT', 'DELETE'])
def history():
    res = {}
    query = request.get_json()
    if request.method == 'GET':
       res = get_history(query['id'], query['start'], query['end'], query['type'])

    if request.method == 'POST':
       res = post_history(query['user_id'], query['start'], query['work_conent'], query['report'], query['type'])

    if request.method == 'PUT':
       res = put_history(query['user_id'], query['start'], query['hang_out'], query['hant_in'], query['work_conent'], query['report'], query['type'])
       
    if request.method == 'DELETE':
       res = delete_history(query['id'])

    return make_response(jsonify(res))


@app.route('/users', methods=['GET'])
def users():
    res = get_users()
    return make_response(jsonify(res))


@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    res = {}
    query = request.get_json()
    if request.method == 'GET':
       res = get_user(query['user_id']) 

    if request.method == 'POST':
       res = post_user(query['name'], query['password'], query['email'], query['enter_date'], query['tags'], query['role'])
   
    if request.method == 'PUT':
       res = put_user(query['name'], query['password'], query['email'], query['enter_date'], query['tags'], query['role'])
       
    if request.method == 'DELETE':
       res = delete_user(query['user_id'])

    return make_response(jsonify(res))


@app.route('/sign_in', methods=['POST'])
def sign_in():
    res = {}
    query = request.get_json()
    if request.method == 'POST':
       res = post_sign(query['email'], query['password'])
    
    return make_response(jsonify(res))

@app.route('/request')
def requests():
    res = {}
    return make_response(jsonify(res))


if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)

