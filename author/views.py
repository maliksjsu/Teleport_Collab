from chef_browser import app
from flask import render_template, redirect, session, request, url_for
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt

@app.route('/auth_login', methods=('GET', 'POST'))
def auth_login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        author = Author.query.filter_by(
            username=form.username.data,
            ).first()
        if author:
            if bcrypt.hashpw(form.password.data, author.password) == author.password:
                session['username'] = form.username.data
                session['is_author'] = author.is_author
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('blog'))
            else:
                error = "Incorrect password"
        else:
            error = "Author not found"
    return render_template('author/auth_login.html', form=form, error=error)

@app.route('/auth_register', methods=('GET', 'POST'))
def auth_register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/auth_success')
    return render_template('author/auth_register.html', form=form)

@app.route('/auth_logout')
def auth_logout():
    session.pop('username')
    return redirect(url_for('blog'))

@app.route('/auth_success')
def auth_success():
    return "Author registered!"

@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in!"