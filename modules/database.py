from flask_sqlalchemy import SQLAlchemy
# from modules.app import flask_app
from modules.app import app


class Hash(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    hash = app.db.Column(app.db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Hash={self.hash}>'
