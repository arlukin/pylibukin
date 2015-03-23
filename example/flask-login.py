#! /usr/local/pythonenv/pylukinlib/bin/python
"""
Demonstrating the login blueprint using flask-login.

"""

__author__ = "daniel.lindh@renter.se"
__copyright__ = "Copyright 2015, Renter AB"

import os
from flask import Flask
from flask.ext.login import login_required

from pylukinlib.flask.blueprint import login


app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,

    # Generate a new secret key every time the wsgi are restarted. This
    # will invalidate all sessions between restarts.
    SECRET_KEY=os.urandom(24)
))

login.init_app(app, "index", {"user": "password"})
app.register_blueprint(login.login_pages)


@app.route('/')
@login_required
def index():
    return 'Hello World! <a href="/logout">logout</a>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)