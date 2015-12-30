import os, time
from flask import Flask, Response, render_template, jsonify
from geojson import Point, Feature, FeatureCollection

app = Flask(__name__)
app.debug = True

ACCESS_KEY = os.environ.get('MAPBOX_ACCESSKEY')

@app.route('/')
def index():
    return render_template('index.html', ACCESS_KEY=ACCESS_KEY)

@app.route('/result')
def process():
    point = Point((-77.0366048812866, 38.89784666877921))
    feature = Feature(geometry=point)
    feature_collection = FeatureCollection([feature])
    return jsonify(result=feature_collection)

@app.route('/process')
def long_running_process():
      def generate():
        for row in range(1, 10):
            yield 'data: Processing \n\n'
            time.sleep(2)
      return Response(generate(), mimetype='text/event-stream')  

app.run(threaded=True)
