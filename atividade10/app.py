import os
from flask import Flask, request, render_template, make_response, redirect, url_for, session
from dotenv import load_dotenv

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    name = request.cookies.get('name')
    visits = request.cookies.get('visits', 0)
    visits = int(visits) + 1

    response = make_response(render_template('index.html', name=name, visits=visits))
    response.set_cookie('visits', str(visits))
    return response

@app.route('/name/<user_name>')
def set_name(user_name):
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name', user_name)
    response.set_cookie('visits', '0')
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123':
            session['user'] = username
            return redirect(url_for('profile'))
        else:
            return "Credenciais inválidas"

    return render_template('login.html')


@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('profile.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)