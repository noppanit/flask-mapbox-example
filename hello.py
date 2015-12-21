import os
from flask import Flask

from flask import jsonify
app = Flask(__name__)
app.debug = True
@app.route('/')
def hello():
      return 'Hello World!'

@app.route('/process')
def process():
      return jsonify(username='fangzhou')
