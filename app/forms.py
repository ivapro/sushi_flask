from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = TextField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
    remember_me = BooleanField('Запомнить меня')


class RegistrationForm(FlaskForm):
    username = TextField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    repeat_password = PasswordField("Повторите пароль", validators=[DataRequired()])

