from flask import Flask
from api.routes import registre_route
from api.config import load_settings
from api.db import db
from api.ext import ma, migrate

app_config = load_settings()


def create_app():
    app = Flask(__name__)

    # Configuring app
    app.config.from_object(app_config)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.url_map.strict_slashes = False

    # Load routes
    registre_route(app)

    return app
