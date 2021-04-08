import time
from flask import Flask, render_template
app = Flask(__name__, static_folder="../../../../../JS/React/GitHub/react-projects/15-cocktails/setup/build", static_url_path='/')




# emulate the root url
@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/hello')
def hello():
    return "hello world"


@app.route('/api/time')
def get_current_time():
    return {'vaqt': time.ctime(time.time())}
