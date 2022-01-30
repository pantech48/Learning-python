from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class ChatMessages(db.Model):
    """Полльзователь."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), nullable=False, comment='Имя пользователя')
    msg = db.Column(db.Text, nullable=False, comment='Текст сообщения')

    def __repr__(self):
        return '<User %r>' % self.username