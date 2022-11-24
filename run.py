from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/categories')
def listCategories():
    result = None
    with open('categories.json','r') as r:
        result = json.load(r)
    return jsonify(result)

@app.route('/category/group')
def categoryGroup():
    result = None
    with open('categoryGroup.json','r') as r:
        result = json.load(r)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
