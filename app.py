from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import db

app = Flask(__name__)
api = Api(app)

class RESTApi(Resource):
    def post(self):
        if 'image' not in request.files:
            return jsonify(message="No image file found")
        image = request.files['image']
        print(image)
        return jsonify(message="POST request received")


class StoreApi(Resource):
    def post(self):
        if 'image' not in request.files:
            return jsonify(message="No image file found")
        image = request.files['image']
        db.store_image(image)
        return jsonify(message="POST request received")

api.add_resource(RESTApi, '/api')
api.add_resource(StoreApi, '/store')

if __name__ == '__main__':
    app.run(debug=True)
