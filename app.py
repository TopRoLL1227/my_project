from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager, login_required, current_user, UserMixin

from db import connect_to_db, add_object_to_database, check_user, get_user_by_username, get_user_by_id

app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

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
        user = get_user_by_username(username)
        if user and check_user(username, password):
            session['user_id'] = user[0]  # Встановлюємо ідентифікатор користувача у сесію
            return redirect(url_for('profile'))
        else:
            return 'Invalid username or password'
    return render_template('login_form.html')



@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f'Welcome {session["user_id"]}! You are now logged in.'
    else:
        return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    import pdb; pdb.set_trace()  # Точка відлагодження
    user_id = session.get('user_id')
    print("Session user_id:", user_id)
    if user_id:
        user = get_user_by_id(user_id)
        if user:
            return render_template('profile.html', user=user)
        else:
            return 'User not found'
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)


# render_template: Це функція, яка використовується для відображення HTML-шаблонів. 
# Вона дозволяє вставляти дані з Python у HTML-шаблон та повертати готовий HTML-код клієнту.

# request: Цей модуль дозволяє отримувати доступ до даних, що надходять від клієнта через HTTP-запити. 
# Наприклад, через цей об'єкт можна отримати дані форми або параметри URL.

# session: Цей модуль використовується для роботи з сесіями в Flask. Він дозволяє зберігати дані між HTTP-запитами того ж самого клієнта.
# Наприклад, для збереження інформації про користувача після того, як він увійшов в систему.

# redirect: Ця функція використовується для перенаправлення клієнта на іншу сторінку або URL. 
# Наприклад, після успішної обробки даних можна перенаправити користувача на його особистий кабінет.

# url_for: Ця функція генерує URL для вказаного маршруту (route). 
# Вона дозволяє уникнути використання жорстких URL-адрес у вашому коді, що полегшує підтримку і зміну URL-адрес в майбутньому.
