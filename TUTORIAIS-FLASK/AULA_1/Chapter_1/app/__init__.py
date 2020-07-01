from flask import Flask        # Imports the Flask instance method
app = Flask(__name__)          # The Flask instance, which will be the main component to handle the routing process
from app import routes         # That's a call to the route file
