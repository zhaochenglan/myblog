# -*- encoding: utf-8 -*-
'''
@File    :   run.py
@Time    :   2020/03/27 10:19:30
@Author  :   edgar.zhao 
@Version :   1.0
@Contact :   1101017794@qq.com
@Desc    :   None
'''

# here put the import lib
from flask import Flask
from flask_script import Manager
from flask import request
from flask import redirect, url_for, Response, jsonify, make_response, session, current_app, render_template, flash
import click
from flask import abort
from form import forms
app = Flask(__name__)
app.secret_key = 'qwerty'
app.debug = True
manager = Manager(app)


with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)

'''
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

'''
@app.cli.command()
def hello():
    click.echo('hello')


@app.route('/')
def index():
    name = request.args.get('name', "Flask")
    return '<h1> hello world ! %s</h1>' % name


@app.route("/h")
def h():
    return redirect(url_for('index2'), code=301)


@app.route('/greet', defaults={'name': 'edgar'})
@app.route('/greet/<name>')
def index2(name):
    return '<h1> hello world! %s</h1>' % name


@app.route('/404')
def not_found():
    abort(404)


@app.route("/cookie")
def cookie():
    response = make_response("abc")
    response.set_cookie('name', 'edgar')

    return response


@app.route('/login2')
def login2():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'test')
        response = '<h1>Hello,%s</h1>' % name
        if 'logged_in' in session:
            response += '[Authenticaed]'
        else:
            response += '[Not Authenticaed]'
        return Response(response)


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('login2'))


@app.route('/logout')
def logout():
    session.pop('logged_in')
    return redirect(url_for('login2'))


@app.context_processor
def init_var():
    return {'name': 'test'}


@app.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    user = {
        'username': 'edgar',
        'age': 27
    }
    movies = [
        {'name': 'A', 'year': '1990'},
        {'name': 'B', 'year': '1992'},
        {'name': 'C', 'year': '1991'},
    ]
    form = forms.LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(request.form.get('username'))
            flash('Welcome')
            return redirect(url_for('watchlist'))
    return render_template('watchlist.html', user=user, movies=movies, form=form)


if __name__ == "__main__":
    manager.run()
