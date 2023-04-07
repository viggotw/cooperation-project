from flask import Flask
from flask_cors import CORS

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from models import db, Comment

app = Flask(__name__)
CORS(app)

N = 0

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()

# Define the endpoints
@app.route('/api/comments', methods=['GET', 'POST'])
def comments():
    print("Comments endpoint called")
    if request.method == 'POST':
        # Create a new comment
        data = request.get_json()
        text = data['text']
        author = data.get('author')
        comment = Comment(text=text, author=author)
        db.session.add(comment)
        db.session.commit()
        return jsonify({'message': 'Comment created successfully'})
    else:
        # Retrieve all comments
        comments = Comment.query.all()
        return jsonify([c.to_dict() for c in comments])


@app.route('/api/hello')
def hello():
    print("Hello endpoint called")
    global N
    N += 1
    return {'message': 'Hello from the backend!', 'N': N}


if __name__ == '__main__':
    print('Starting Flask server...')
    app.run(debug=True)
