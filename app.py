from flask import Flask, g, jsonify, render_template

import config
import models
from resources.todos import todos_api

app = Flask(__name__)
app.register_blueprint(todos_api, url_prefix='/api/v1')

@app.route('/api/v1/todos/', methods=['GET'])
def my_todos():
    return jsonify({'todos': todos})

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
