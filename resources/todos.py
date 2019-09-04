from flask import jsonify, Blueprint, abort

from flask_restful import (Resource, Api, reqparse,
                           inputs, fields, marshal,
                           marshal_with, url_for)

import models

todos_fields = {
    'id': fields.Integer,
    'name': fields.String
}

def todo_or_404(todo_id):
    """ Function to handle 404 error """
    try:
        todo = models.Todo.get(models.Todo.id == todo_id)
    except models.Todo.DoesNotExist:
        abort(404)
    else:
        return todo


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
        todos = [marshal(todo, todos_fields)
                for todo in models.Todo.select()]
        return todos

    @marshal_with(todos_fields)
    def post(self):
        args = self.reqparse.parse_args()
        todo = models.Todo.create(**args)
        return (todo, 201, {
                'location': url_for('resources.todos.todo', id=todo.id)}
               )


class Todo(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help=('No TODO provided'),
            location=['form', 'json']
        )
        super().__init__()

    @marshal_with(todos_fields)
    def get(self, id):
        """ Get a given TODO """
        return todo_or_404(id)

    @marshal_with(todos_fields)
    def put(self, id):
        """ Editting of posted TODOS"""
        args = self.reqparse.parse_args()
        query = models.Todo.update(**args).where(models.Todo.id==id)
        query.execute()
        return (models.Todo.get(models.Todo.id==id), 200,
                {'location': url_for('resources.todos.todo', id=id)})

    def delete(self, id):
        """ Delete a specific TODO"""
        try:
            todo =  models.Todo.select().where(models.Todo.id==id).get()
        except models.Todo.DoesNotExist:
            abort(404)
        todo.delete_instance()
        return ('', 204, {'location': url_for('resources.todos.todos')})


todos_api = Blueprint('resources.todos', __name__)
api = Api(todos_api)
api.add_resource(
    TodosList,
    '/todos',
    endpoint='todos'
)
api.add_resource(
    Todo,
    '/todos/<int:id>',
    endpoint = 'todo'
)
