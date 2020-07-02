from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# '/' and '/index' route, defined to return a username as a view function response
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Linus Torvald'}
    return render_template('index.html', title='Home', user=user)

# '/login' The login route a instance with the class LoginForm is created.
# If the required fields as fullfilled and the necessary ones loaded as well, the validation
# is completed, otherwise return to login page.  The flashing system basically makes it possible to record a 
# message at the end of a request and access it next request and only next request. 
# This is usually combined with a layout template that does this.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
