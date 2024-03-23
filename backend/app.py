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


@app.route('/api/items', methods=['GET'])
def get_data():
    return jsonify(arr)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
