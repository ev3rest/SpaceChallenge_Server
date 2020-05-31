from modules.database import Hash
from modules.app import app
import datetime


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
    risk = "No risk"
    now = datetime.datetime.utcnow()
    for item in q.all():
        created_at = item.created_at
        if created_at - now > datetime.timedelta(days=14):
            risk = "Low risk"
        else:
            return "High risk"
    return risk
