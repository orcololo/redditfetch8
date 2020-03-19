from flask import Flask
from flask_restful import Resource, Api
from helpers.reddit import getSub2

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return getSub2('gonewild', 20)


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
