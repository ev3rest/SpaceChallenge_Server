from modules.database import Hash
from modules.app import app


def add_to_db(hashcodes: str):
    ok = True
    for hashcode in hashcodes:
        try:
            hash_obj = Hash(hash=hashcode)

            app.db.session.add(hash_obj)
            app.db.session.commit()
        except Exception:
            ok = False
    return ok


def is_in_db(hashcodes: list):
    q = Hash.query.filter(Hash.hash.in_(hashcodes))
    if q.count() > 0:
        return True
    return False
