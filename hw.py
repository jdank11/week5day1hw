from flask import Flask, request

from uuid import uuid4

app= Flask(__name__)

users = {
    'car1': {
        'make': 'acura',
        'year': '2024'
    },
    'car2': {
        'make': 'honda',
        'year': '2000'
    }
}

mods = {
    '1': {
        'tint': '20%',
        'user_id': 'car1'
    },
    '2': {
        'body': '5%',
        'user_id': 'car2'
    }
}


@app.route('/user')
def user():
    return { 'users': list(users.values())} , 200

@app.route('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] =json_body
    return { 'your car' : f'{json_body["make"] + json_body["year"]} created'}, 201

@app.put('/user')
def update_user():
    return

@app.delete('/user')
def delete_user():
    return

#######################

@app.get('/mods')
def get_mods():
    return { 'mods': list(mods.values())} 

@app.post('/mods')
def create_mods():
    json_body = request.get_json()
    users[uuid4()] =json_body
    return { 'your mods' : f'{json_body["tint"]} tint'}, 201

@app.put('/mods')
def update_mods():
    return

@app.delete('/mods')
def delete_mods():
    return