from flask import render_template # Importing the instance method render_template for rendering the front end part
from app import app               # Importing th Flask app instance

@app.route('/')
@app.route('/index')              # Defining two enpoints for the view
def index():                      # View function to handle  the two endpoints
    user = {'username': 'Linus Torvald'}
    return render_template('index.html', title='HOME', user=user)

# In this routing, a use is created with a dictionary data structure. The instance method render_template is taking as
# arguments: the template name (index.html), the title to the header, and returning a user created inside the view function