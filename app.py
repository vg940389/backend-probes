"""Example of flask main file."""
from flask import Flask
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return "Hello, KubeRocketCI!"

# Readiness probe – controls traffic
@app.route('/api/readiness')
def readiness():
    return {"status": "readiness-ok"}, 200

# Liveness probe – controls restart
@app.route('/api/liveness')
def liveness():
    return {"status": "liveness-ok"}, 200

if __name__ == '__main__':
    app.run()
