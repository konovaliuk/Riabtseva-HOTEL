from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import InputRequired, Length, Email, Regexp, DataRequired

# from app import app
# from flask import render_template, url_for, redirect, request, flash, Flask
# from flask_login import current_user, login_user, logout_user, LoginManager
# from services import get_user_by_id, create_user, validate_login
# from encode import *

__all__ = ['LoginForm', 'SignUp', 'Booking']


class LoginForm(FlaskForm):
    email = StringField('Пошта',
                        validators=[Length(max=30, message='Занадто довга поштова скринька!'),
                                    Email(message='Пошта має бути заповнена!'),
                                    Regexp('^[a-z A-Z 0-9 ]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$',
                                           message='Не валідний емейл!!'), ])

    password = PasswordField('Пароль', validators=[InputRequired(message='Пароль не має бути порожнім!'),
                                                   Length(min=4, max=15,
                                                          message='Довжина паролю має бути від 4 до 15 символів!')])
    remember = BooleanField('Запам\'ятати мене')


class SignUp(FlaskForm):
    email = StringField('Пошта',
                        validators=[Length(max=30, message='Занадто довга поштова скринька!'),
                                    Email(message='Пошта має бути заповнена!'),
                                    Regexp('^[a-z A-Z 0-9 ]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$',
                                           message='Не валідний емейл!!'), ])

    first_name = StringField('Ім\'я',
                             validators=[InputRequired(message='Ім\'я не має бути порожнім!'),
                                         Length(min=4, max=15, message='Довжина імені має бути від 4 до 15 символів!'),
                                         Regexp('[a-z A-Z а-я А-Я 0-9]+', message='Ім\'я має містити букви!')])

    last_name = StringField()
    password = PasswordField('Пароль',
                             validators=[InputRequired(message='Пароль не має бути порожнім!'),
                                         Length(min=4, max=15,
                                                message='Довжина паролю має бути від 4 до 15 символів!')])


class Booking(FlaskForm):
    room_type = SelectField('Select Room Preference',
                            choices=[('normal', 'Normal'), ('luxe', 'Luxe')], validators=[DataRequired()],  render_kw={"class": "form-control form-control-lg", "id": "typeRoom_typeX"})

    check_in_date = DateField('Check-in Date',
                              validators=[DataRequired()],
                              format='%Y-%m-%d')

    check_out_date = DateField('Check-out Date',
                               validators=[DataRequired()],
                               format='%Y-%m-%d')

    number_people = IntegerField('Number people',
                                 validators=[InputRequired(),
                                             Length(max=5, message='Number of people cannot exceed 5.')])
