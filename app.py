from flask import Flask
from flask_restful import Resource, Api
from helpers.reddit import getSub2

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        print(type(getSub2('gonewild', 10)))
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
