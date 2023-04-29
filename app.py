from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import db

app = Flask(__name__)
api = Api(app)

class RESTApi(Resource):
    def get(self):
        return jsonify(message="GET request received")

    def post(self):
        if 'image' not in request.files:
            return jsonify(message="No image file found")
        image = request.files['image']
        db.store_image(image)
        return jsonify(message="POST request received")

    def put(self):
        return jsonify(message="PUT request received")

    def delete(self):
        return jsonify(message="DELETE request received")

api.add_resource(RESTApi, '/api')

if __name__ == '__main__':
    app.run(debug=True)
