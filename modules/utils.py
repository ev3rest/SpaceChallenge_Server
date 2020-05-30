from modules.database import Hash
from modules.app import app


def insert(hashcode: str):
    hash_obj = Hash(hash=hashcode)

    app.db.session.add(hash_obj)
    app.db.session.commit()
