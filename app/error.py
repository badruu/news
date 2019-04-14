from flask import render_template
from app import app

@app.errorhandler(404)
def error(error):
    '''
    Function to render the 404 page
    '''
    return render_template('error.html'),404