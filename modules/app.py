from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

from run import conf


class App:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(App, cls).__new__(cls)
        return cls.instance

    app = Flask(__name__)

    db_str = "postgres://{username}:{password}@{host}:{port}/{db_name}".\
        format(username=conf.db_username,
               password=conf.db_password,
               host=conf.db_host,
               port=conf.db_port,
               db_name=conf.db_name)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_str
    db = SQLAlchemy(app)


app = App()
from modules.utils import (
    add_to_db,
    is_in_db
)


@app.app.route('/insert_contacts', methods=['POST'])
def insert():
    """
    This function writes hashcode of the infected people
    to the database

    :param hashcode: hash of type str
    :return:
    """

    args = request.args
    hashes = json.loads(args['hashes'])
    response = add_to_db(hashes['data'])
    return {"response": response}


@app.app.route('/check_contacts', methods=['POST'])
def check():
    """
    This function finds hashcodes in the database

    :param hashcodes: [hash1, hash2, ...]
    :return:
    """

    args = request.args
    hashes = json.loads(args['hashes'])

    response = is_in_db(hashes['data'])

    return {'response': response}


def start():
    app.app.run(debug=conf.debug,
                host=conf.flask_host,
                port=conf.flask_port)
