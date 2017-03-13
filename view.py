from flask import Flask, jsonify, request
from models import Client, Books, Ganre, Autors, Authors_Books, initialize
from playhouse.shortcuts import model_to_dict


app = Flask(__name__)

@app.route('/', methods=['POST'])
def create_student():
    return jsonify({'id': 20}), 201

@app.route('/api/students',methods=['GET'])
def get_students():
    return jsonify({'status':'qwer'}), 201


@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    return jsonify({'status':'qwer'}), 201

@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    return jsonify({'status':'qwer'}), 201

@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_students(id):
    return jsonify({'status':'qwer'}), 201


if __name__ == '__main__':
    initialize()
    app.run(use_reloader=True)