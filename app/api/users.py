# -*- coding: utf-8 -*-
"""
    app.api.users
    ~~~~~~~~~~~~~~~~~~

    User endpoints
"""

from flask import Blueprint
from flask_login import current_user

from ..models import User
from . import route

bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""
    return current_user._get_current_object()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    user = User.query.get_or_404(user_id)
    return user
