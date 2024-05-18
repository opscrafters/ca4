from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://root:example@db:27017/")
db = client["test"]

@app.route('/api/data', methods=['GET'])
def get_data():
    data = db.collection.find_one()
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
