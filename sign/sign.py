#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# import functools

from flask import Blueprint
from flask import g
from flask import jsonify
from flask import render_template
from flask import request
from flask import session
from flask import url_for
# from werkzeug.security import check_password_hash
# from werkzeug.security import generate_password_hash

from db import get_user, register_db

bp = Blueprint("sign", __name__, url_prefix="/sign")


# def login_required(view):
#     """View decorator that redirects anonymous users to the login page."""

#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for("sign.login"))

#         return view(**kwargs)

#     return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user email is stored in the session, load the user object from
    the database into ``g.user``."""
    email = session.get("email")

    if email is None:
        g.user = None
    else:
        g.user = (
            # 从数据库中获取用户信息
            # get_db().execute("SELECT * FROM user WHERE email = ?", (email,)).fetchone()
        )


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.

    Validates that the email is not already taken. Hashes the
    password for security.
    """
    res = {}
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        res = register_db(email, password)

    return res


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user email to the session."""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = get_user(email, password)

        if user is None:
            error = "Incorrect email."
        elif not user["password"] == password:
            error = "Incorrect password."

        if error is None:
            # store the user email in a new session and return to the index
            session.clear()
            session["email"] = user["email"]
            return jsonify({"re": 501})

    return jsonify({"re": 200})


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user email."""
    session.clear()
    return jsonify({"re": 200})
