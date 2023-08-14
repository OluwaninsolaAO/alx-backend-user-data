#!/usr/bin/env python3
"""A simple python flask application module"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index_page() -> str:
    """6. Basic Flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """Create new user in database"""
    attrs = ['email', 'password']
    data = {}
    for attr in attrs:
        if attr in request.form:
            data.update({attr: request.form.get(attr)})
        else:
            return jsonify({"message": "Bad request!"}), 400
    try:
        user = AUTH.register_user(**data)
        return jsonify({"email": user.email,
                        "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
