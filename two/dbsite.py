from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase

DEBUG = True
SECRET_KEY = '528224ac031b0b036eab49ef45cfd13e3da1fa9c'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', "r") as f:
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
    return render_template('index.html', menu=dbase.get_menu(), posts=dbase.get_posts_annonce())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_post(request.form["name"], request.form["post"])
            if not res:
                flash("Ошибка добавления статьи", category='error')
            else:
                flash("Статья добавлена успешно", category='success')
        else:
            flash("Ошибка добавления статьи", category='error')

    return render_template('add_post.html', menu=dbase.get_menu(), title="Добавление статьи")


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)

    title, post = dbase.get_post(id_post)
    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run()



