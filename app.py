from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class RESTApi(Resource):
    def post(self):
        data = request.get_json()
        if 'image' not in data:
            return jsonify(message="No image provided"), 400
        image = data['image']
        return jsonify(message="Image uploaded successfully")

api.add_resource(RESTApi, '/api')

if __name__ == '__main__':
    app.run(debug=True)