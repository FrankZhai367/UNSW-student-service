#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from flask import jsonify

def get_user(email, password):
    # 从数据库中获取用户信息
    return {"email": "Z5277229@ad.unsw.edu.au", "password": "Z5277229@ad.unsw.edu.au"}

def register_db(email, password):
  error = None

  if not email:
      error = "email is required."
  elif not password:
      error = "Password is required."
#   elif (
#       # 如果从数据库中获取到用户信息
#   ):
#       error = "User {0} is already registered.".format(email)

  if error is None:
      return jsonify({"re": 200})
  else:
    return jsonify({"re": 501})