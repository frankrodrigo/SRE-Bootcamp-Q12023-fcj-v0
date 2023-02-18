from flask import Flask
from flask import jsonify
from flask import request
from methods import Token, Restricted
from functools import wraps
import jwt
from dbconnect import db_connection

app = Flask(__name__)
login = Token()
protected = Restricted()
queries = db_connection()

app.config['SECRET-KEY'] = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Missing Token!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid Toekn!'}), 403
        return func(*args, **kwargs)
    return wrapped


@app.route("/testdb")
def get_data():
    return queries.db_query_test()


# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form['username']
    password = request.form['password']
    res = {
        "data": login.generate_token(username, password)
    }
    return jsonify(res)


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
@check_for_token
def url_protected():
    auth_token = request.headers.get('Authorization')
    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
