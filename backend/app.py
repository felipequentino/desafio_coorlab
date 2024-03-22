from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# test data
items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    for item in items:
        if item['id'] == item_id:
            item.update(request.json)
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for index, item in enumerate(items):
        if item['id'] == item_id:
            del items[index]
            return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
