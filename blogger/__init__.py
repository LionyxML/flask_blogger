import os

from flask import Flask

def create_app(test_config=None):
    # create the app and configure it
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blogger.sqlite'),
    )

    if test_config is None:
        # when not testing, load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello there!
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app

