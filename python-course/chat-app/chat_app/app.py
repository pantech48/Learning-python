from flask import Flask, render_template, url_for, redirect, session, request
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy


# 1. Создать экземпляр приложения
app = Flask(__name__, instance_relative_config=True)

# 2. Прочитать конфигурационные параметры
app.config.from_pyfile('config.py', silent=True)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.sqlite3'
db = SQLAlchemy()

class ChatMessages(db.Model):
    """Полльзователь."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), nullable=False, comment='Имя пользователя')
    msg = db.Column(db.Text, nullable=False, comment='Текст сообщения')

    def __repr__(self):
        return '<User %r>' % self.username


# 3. Инициализация расширений
db.init_app(app)

# Создает все таблицы в БД
db.create_all(app=app)

socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    print(session)
    username = None
    if session.get("username"):
        username = session.get("username")
    return render_template('index.html', username=username)

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))

@socketio.on('message')
def handleMessage(data):
    print(f"Message: {data}")
    send(data, broadcast=True)

    message = ChatMessages(username=data['username'], msg=data['msg'])
    db.session.add(message)
    db.session.commit()


if __name__ == '__main':
    socketio.run(app)
