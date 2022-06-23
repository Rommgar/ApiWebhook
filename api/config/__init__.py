import os
from .settings import *


def load_settings():
    app_env = os.getenv('FLASK_ENV', 'development').lower()
    settings_switch = {
        'development': DevelopmentSettings,
        'testing': TestingSettings,
        'production': ProductionSettings
    }
    settings = settings_switch.get(app_env, DevelopmentSettings)
    return settings()
