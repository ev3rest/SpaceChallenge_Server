from modules import app as main_app

from config import Config
conf = Config(environment='dev')


if __name__ == "__main__":
    main_app.start()
