import functools

from flask import(
    Blueprint, flash, g, render_template, request, url_for, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.route('/register', methods=['GET', 'POST'])
# def register():
    #TODO: realizar la logica para dar inicio de sessión y traer la información del USER.
    