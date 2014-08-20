# -*- coding: utf-8 -*-
"""
    onboarder
    ~~~~~~~~
    users.forms
"""

from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms import TextField, PasswordField, validators, TextAreaField, \
    SelectField, SelectMultipleField, HiddenField, RadioField, BooleanField, \
    FileField
from wtforms.validators import DataRequired, ValidationError, Required, \
    Optional, Length, URL, Email, Regexp

from ..models import User
from ..core import db

userForm = model_form(User, db.session)


class userSettingsForm(Form):
    name = TextField('Full Name', validators=[Required()])
    email = TextField('Email', validators=[Email(), Required()])
    location = TextField(
        'Where are you located?',
        validators=[Required(), Length(min=-1, max=255)],
        description='Ex. San Francisco, California')


class createUserBasicForm(Form):
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Email(), Required()])
    password = PasswordField('Password', validators=[
        Required(), Length(min=6, max=255)])
    sitdown_id = HiddenField('Sitdown Id', validators=[Optional()])

    def validate_email(form, field):
        # Check to make sure email is unique
        if User.query.filter_by(email=field.data).count():
            raise ValidationError('Email already exists')


class createUserForm(Form):
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Email(), Required()])

    def validate_email(form, field):
        # Check to make sure email is unique
        if User.query.filter_by(email=field.data).count():
            raise ValidationError('Email already exists')


class createUserExtendedForm(Form):
    name = TextField('Name', validators=[Required()])
    business_name = TextField('Business Name', validators=[Optional()])
    email = TextField('Email', validators=[Email(), Required()])
    username = TextField('Username', validators=[
        Required(), Length(min=5, max=20)])
    gravatar = TextField('Gravatar', validators=[Optional()])

    def validate_username(form, field):
        # Check to make sure email is unique
        if User.query.filter_by(username=field.data).count():
            raise ValidationError('Username already exists')

    def validate_email(form, field):
        # Check to make sure email is unique
        if User.query.filter_by(email=field.data).count():
            raise ValidationError('Email already exists')


class aboutUserForm(Form):
    name = TextField(validators=[Optional()])
    business_name = TextField(validators=[Optional()])
    gangster_name = TextField(validators=[Optional()])
    profile_photo = TextField(validators=[Optional()])
    location = TextField(validators=[Optional()])
    rating = TextField(validators=[Optional()])
    hireable = BooleanField(validators=[Optional()])
    twitter_handle = TextField(validators=[Optional()])
    homepage = TextField(validators=[Optional()])
    claim = TextField(validators=[Optional()])
    bio = TextAreaField(validators=[Optional()])


class detailUserForm(Form):
    tags = TextField(validators=[Optional()])
    workmob_rank = TextField(validators=[Optional()])
    completed_projects = TextField(validators=[Optional()])
    github_followers = TextField(validators=[Optional()])
    stackoverflow_rep = TextField(validators=[Optional()])
    projects = TextField(validators=[Optional()])
    comments = TextField(validators=[Optional()])
    reviews = TextField(validators=[Optional()])
    images = TextField(validators=[Optional()])


class kickstartProfileForm(Form):
    name = TextField(validators=[Required()])
    gangster_name = TextField(validators=[Optional()])
    email = TextField('Email', validators=[Email(), Required()])
    username = TextField('Username', validators=[
        Required(), Length(min=5, max=20)])

    def validate_username(form, field):
        # Check to make sure email is unique
        if User.query.filter_by(username=field.data).count():
            raise ValidationError('Username already exists')

    def validate_email(form, field):
        # Check to make sure email is unique
        if User.query.filter_by(email=field.data).count():
            raise ValidationError('Email already exists')
