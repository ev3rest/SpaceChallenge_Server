# General import
import configparser
import os


class Config:
    def __new__(cls, environment='prod'):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self, environment='prod'):
        config_parser = configparser.RawConfigParser()
        path_to_cur_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = f'{path_to_cur_dir}/config.properties'
        config_parser.read(config_file_path)

        self.db_name = config_parser.get(environment, 'database.name')
        self.db_host = config_parser.get(environment, 'database.host')
        self.db_port = config_parser.get(environment, 'database.port')
        self.db_username = config_parser.get(environment, 'database.username')
        self.db_password = config_parser.get(environment, 'database.password')

        self.flask_host = config_parser.get(environment, 'flask.host')
        self.flask_port = config_parser.get(environment, 'flask.port')
        self.debug = config_parser.get(environment, 'flask.debug')
