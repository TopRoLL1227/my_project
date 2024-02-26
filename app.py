from flask import Flask, render_template, request, session, redirect, url_for
from db import connect_to_db, add_object_to_database, check_user

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('add_object_form.html')

@app.route('/add_object', methods=['POST'])
def add_object():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return 'Please fill out all fields'
        if len(username) < 3 or len(password) < 6:
            return 'Username must be at least 3 characters long and password must be at least 6 characters long'
        add_object_to_database(username, password)
        return 'Object added successfully'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login_form.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Welcome {session["username"]}! You are now logged in.'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)







