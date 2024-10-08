from flask import Flask, render_template, url_for, request, flash, session, redirect, g
import sqlite3
import os
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '2b71c1ed2dc317653673b285fcbe70da5a616dce'

app = Flask(__name__)
app.config.from_object(__name__)

# app.config['SECRET_KEY'] = 'rtertg465464fdfhg8465464hgfhfgh113103'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"}
]


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title="Главная", menu=dbase.get_menu(), posts=dbase.get_posts_annonce())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category="error")
            else:
                flash("Статья добавлена успешно", category='success')
        else:
            flash('Ошибка добавления статьи', category="error")

    return render_template('add_post.html', menu=dbase.get_menu(), title="Добавление статьи")


@app.route("/post/<alias>")
def show_post(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(alias)
    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О нас", menu=menu)


@app.route('/profile/<username>')
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', **context, title="Обратная связь", menu=menu)
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged111' in session:
        return redirect(url_for('profile', username=session['userLogged111']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123456':
        session['userLogged111'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged111']))
    return render_template('login.html', title="Авторизация", menu=menu)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
