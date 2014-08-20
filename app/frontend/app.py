# -*- coding: utf-8 -*-
"""
    onboarder
    ~~~~~~~~
    app.views (app)

"""
import re
import datetime
import requests
import json

from pprint import pprint
from sqlalchemy.sql.expression import func

from flask import Blueprint, render_template, flash, redirect, url_for, \
    request, abort, jsonify, make_response, session
from flask_security import login_required, current_user, login_user, \
    logout_user, roles_required, user_registered
from flask_security.utils import encrypt_password
from flask_restless.helpers import to_dict

from . import route
from ..core import db
from ..models import User
from ..forms import userSettingsForm, kickstartProfileForm
from ..helpers import id_generator, gravatar

from underscore import _


bp = Blueprint('app', __name__)


@route(bp, '/')
def index():
    """Returns the index."""
    return render_template('index.html')


@route(bp, '/preferences', methods=['GET', 'POST'])
@login_required
def preferences():
    """Allows user to change account prefs"""
    form = userSettingsForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash('Successfully updated your profile', 'success')
    return render_template('preferences.html', form=form)
