from modules.app import app


class Hash(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    hash = app.db.Column(app.db.String(80), unique=True, nullable=False)

    query = app.db.session.query_property()

    def __repr__(self):
        return f'<Hash={self.hash}>'
