from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    title ='404 page'
    return render_template('404.html',title=title),404