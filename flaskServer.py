from flask import Flask, url_for, request, render_template, jsonify
from MyDBManager import *

app = Flask(__name__)
dbManager = MyDBManager()


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/movies/', methods=['GET'])
@app.route('/movies/<id>', methods=['GET'])
def fetch_movies(id=None):
    if id is None:
        return jsonify(dbManager.fetch_movies())
    else:
        # print(id)
        return jsonify(dbManager.fetch_movies(id=id))


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))http://localhost:5000/hello/whatsup


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
