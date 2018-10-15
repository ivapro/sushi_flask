from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user
import sqlite3


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    with sqlite3.connect("users.db") as con:
        cursor = con.cursor()
        form = LoginForm()
        if form.validate_on_submit():

            cursor.execute("SELECT COUNT(*) FROM user WHERE username=?", [form.username.data])
            count = cursor.fetchone()[0]

            if count == 0:
                flash('Пользователь не найден!')
                return redirect(url_for('login'))
            cursor.execute("SELECT password FROM user WHERE username=?",[form.username.data])
            if check_password_hash(cursor.fetchone()[0],form.password.data):
                flash('Вход выполнен!')
                return redirect(url_for('login'))
            else:
                flash('Введен не верный пароль!')
                return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    with sqlite3.connect("users.db") as con:
        form = RegistrationForm()
        cursor = con.cursor()

        if form.validate_on_submit():
            if len(form.password.data) < 6:
                flash('Пароль должен быть длиной не менее 6 символов!')
                return redirect(url_for('registration'))
            if form.password.data != form.repeat_password.data:
                flash('Пароли не совпадают!')
                return redirect(url_for('registration'))

            cursor.execute("SELECT COUNT(*) FROM user WHERE username=?", [form.username.data])
            count = cursor.fetchone()[0]

            if count > 0:
                flash('Пользователь с такой почтой уже зарегестрирован!')
                return redirect(url_for('registration'))

            # cursor.execute("""SET IDENTITY_INSERT user ON""")
            cursor.execute("INSERT INTO user(username, password) VALUES(?,?)", (form.username.data,
                            generate_password_hash(form.password.data)))
            # cursor.execute("SET IDENTITY_INSERT user OFF")
            con.commit()

    return render_template('registration.html', form=form)


@app.route('/rolli')
def rolli():
    return render_template('rolli.html')


@app.route('/sushi')
def sushi():
    return render_template('sushi.html')
