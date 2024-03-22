from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('../app/data.json') as f:
    data = json.load(f)

arr = []

for item in data["transport"]:
    arr.append(item)

print(arr[4]["city"])

@app.route('/api/items', methods=['GET'])
def get_data():
    return jsonify(arr)

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    arr.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    for item in data:
        if item['id'] == item_id:
            item.update(request.json)
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for index, item in enumerate(data):
        if item['id'] == item_id:
            del data[index]
            return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
