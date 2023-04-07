from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

N = 0

@app.route('/api/hello')
def hello():
    global N
    N += 1
    return {'message': 'Hello from the backend!', 'N': N}

if __name__ == '__main__':
    print('Starting Flask server...')
    app.run(debug=True)
