import importlib
import os


def registre_route(app):
    for file in os.listdir(os.path.dirname(__file__)):
        if '__' not in file:
            bp = importlib.import_module('.{}'.format(file.removesuffix('.py')), __name__)
            bp.blueprint.url_prefix = app.config.get('API_PREFIX_URL')
            app.register_blueprint(bp.blueprint)
