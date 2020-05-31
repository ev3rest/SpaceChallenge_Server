from modules.database import Hash
from modules.app import app


def add_to_db(hashcode: str):
    hash_obj = Hash(hash=hashcode)

    app.db.session.add(hash_obj)
    app.db.session.commit()


def is_in_db(hashcodes: list):
    pass
