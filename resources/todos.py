from flask import jsonify, Blueprint, abort

from flask.ext.restful import (Resource, Api, reqparse,
                               inputs, fields, marshal,
                               marshal_with, url_for)

import models

todos_fields = {
    'id': fields.Integer,
    'name': fields.String
}


class TodosList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help=('No TODO provided'),
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        todos = [marshal(todos_fields) for todo in models.Todo.select()]
        return {'todos': todos}

todos_api = Blueprint('resources.todos', __name__)
api = Api(todos_api)
api.add_resource(
    TodosList,
    '/api/v1/todos',
    endpoint='todos'
)
