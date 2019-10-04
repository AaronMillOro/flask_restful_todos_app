from peewee import *


DATABASE = SqliteDatabase('todos.sqlite')


class Todo(Model):
    name = CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()
