from app import app          # Importing the Flask instance


@app.route('/')              # Defining two enpoints for the view function index
@app.route('/index')
def index():                 # View function to handle  the two endpoints

    return "Hello, World!"   # Response to the get request
