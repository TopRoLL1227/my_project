
# У фреймворку Flask на Python маршрут (route) визначає, як програма реагує на запити веб-клієнтів до певного URL. 
# Коли ви створюєте веб-додаток з використанням Flask, ви визначаєте функції, які виконуються при запитах на певні URL-адреси.
# Наприклад, якщо ви хочете мати сторінку /hello, ви створюєте маршрут для неї. При запиті до цього URL, Flask викличе певну функцію, 
# яка буде відповідати на цей запит. Ось приклад визначення маршруту в Flask:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()




# У цьому прикладі, якщо ви запитаєте URL /hello, Flask викличе функцію hello(), яка поверне рядок "Hello, World!". 
# Таким чином, маршрути допомагають організувати роботу вашого веб-додатку і вказують, які дії виконувати при різних запитах до веб-сервера.






