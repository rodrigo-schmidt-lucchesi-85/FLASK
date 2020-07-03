from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# '/' and '/index' route, defined to return a username as a view function response
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Linus Torvald'}
    return render_template('index.html', title='Home', user=user)

# In the login route ('/login' ) form, an instance from the LoginForm class is created. 
# If the required fields are fulfilled, the validation is completed and the home page is 
# redirected. Otherwise, return to the login page.  The flashing system is a way to 
# interact with the user to map which actions were taken.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
