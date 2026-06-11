from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mallory'}
    posts = [
        {
            'author': {'username': 'Bernardo'},
            'body': 'Beautiful day in San Diego!'
        },
        {
            'author': {'username': 'Paige'},
            'body': 'The Backrooms movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)