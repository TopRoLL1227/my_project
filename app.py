# Створення HTML-форм
from flask import Flask, render_template, request
import psycopg2
# render_template - це функція у Flask, яка використовується для відображення HTML-шаблонів. Вона дозволяє вам передавати дані з вашого Python-коду 
# в HTML-шаблон, щоб створювати динамічні веб-сторінки.

# Основна задача render_template полягає в тому, щоб зчитати HTML-файл з папки templates вашого проекту, 
# обробити його за допомогою Jinja2 (шаблонізатора, що використовує Flask) та повернути результуючий HTML-код.

# Наприклад, якщо ви викликаєте render_template('index.html'), Flask знайде файл index.html у вашій папці templates, 
# обробить його та поверне веб-сторінку, яку ви можете побачити у вашому браузері.


app = Flask(__name__)  # Тут ми створюємо екземпляр класу Flask із змінною ім'я app. __name__ - це спеціальна змінна Python, 
                       # яка автоматично встановлюється Python для модуля, в якому вона використовується. 
                       # Вона використовується Flask для визначення розташування пакетів та ресурсів, таких як шаблони та статичні файли.


def add_object_to_database(username, password):  # Ця функція призначена для додавання нового об'єкта до бази даних.
    conn = None  # Ініціалізуємо змінну conn перед спробою використання у блоках try і finally
    try:                                        # вона приймає два параметри: name (ім'я об'єкта) і password (опис об'єкта).
        conn = psycopg2.connect(  # В середовищі try здійснюється підключення до бази даних PostgreSQL за допомогою функції psycopg2.connect()
            dbname="my_project",
            user="postgres",
            password="4591",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()  # Після успішного підключення до бази даних створюється курсор (cursor), який дозволяє виконувати SQL-запити до бази даних. 
                                # У цьому випадку виконується SQL-запит INSERT, який додає новий запис до таблиці бази даних. 
                                # Значення для name та password передаються як параметри запиту, щоб запобігти SQL-ін'єкції.
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()  # Після виконання SQL-запиту викликається метод commit() для збереження змін у базі даних.
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Error adding object to database:", error)
    finally:  # У блоку finally здійснюється закриття курсора та з'єднання з базою даних. Це важливо для звільнення ресурсів та запобігання витоку пам'яті.
        if conn:  # У випадку, якщо під час виконання коду в середовищі try виникає будь-яка помилка, вона обробляється в блоку except. У цьому випадку будь-яка помилка, яка виникає під час виконання SQL-запиту, виводиться у консоль за допомогою функції print().
            cursor.close()
            conn.close()


@app.route('/')  # Це декоратор маршрутизатора Flask, який вказує Flask, який URL-шлях повинен відповідати даній функції. 
                 # У цьому випадку ми використовуємо /, тобто кореневий URL, що означає, що функція index() буде викликана, 
                 # коли користувач перейде за адресою http://адреса_сайту/.
def index():  # Це визначення функції Python з назвою index. Ця функція буде викликана, коли користувач перейде на URL-шлях /.
    return render_template('add_object_form.html')  # В цьому рядку ми використовуємо функцію render_template, що надається Flask. 
                                          # Ми передаємо їй ім'я шаблону index.html. Flask автоматично шукає цей файл у папці templates, 
                                          # як пояснено раніше, обробляє його і повертає веб-сторінку, яку відображає ваш браузер.
# Отже, ця функція виконує додавання нового об'єкта до вашої бази даних PostgreSQL, а також надійно обробляє можливі помилки, які можуть виникнути під час цього процесу.


@app.route('/add_object', methods=['POST', 'GET'])   # Цей декоратор вказує Flask, що функція add_object() повинна бути викликана, коли HTTP-запит приходить на URL-адресу '/add_object' методом POST.
def add_object():  # Ця функція визначає логіку обробки запиту.
    if request.method == 'POST':
        username = request.form['username']  # Витягуємо дані з POST-запиту. У цьому випадку очікується, що дані відправлені у форматі форми і містять поле 'username'.
        password = request.form['password']  # Аналогічно до попереднього рядка, витягуємо пароль.
        if not username or not password:
            return 'Please fill out all fields'
        if len(username) < 3 or len(password) < 6:
            return 'Username must be at least 3 characters long and password must be at least 6 characters long'
        add_object_to_database(username, password)
        return 'Object added successfully'
    else:
        return 'Method not allowed'


if __name__ == '__main__':  # Умова if __name__ == '__main__': перевіряє, чи файл app.py був запущений безпосередньо, а
    app.run(debug=True)     # не імпортований як модуль у інший файл. Якщо це так, то метод run() запускає вбудований сервер Flask, 
                            # який слухатиме вхідні з'єднання на порту 5000. Параметр debug=True дозволяє включити режим налагодження, 
                            # що допомагає знайти помилки під час розробки.
    
# Отже, коли користувач переходить за адресою http://адреса_сайту/, Flask викликає функцію index(), яка повертає HTML-сторінку, 
# згенеровану з файлу index.html, розташованого у папці templates.



