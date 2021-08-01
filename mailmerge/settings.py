# -*- coding: utf-8 -*-
import os
import importlib
from typing import Type, Union

"""
設定檔
"""


class Config(object):
    ACTION_OPTION_PDF = "pdf"
    ACTION_OPTION_HTML = "html"
    ACTION_OPTION_EMAIL = "email"
    ACTION_OPTIONS = [
        ACTION_OPTION_PDF,
        ACTION_OPTION_HTML,
        ACTION_OPTION_EMAIL
    ]

class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass



config_mappings = {
    ".dev": DevConfig,
    ".prod": ProdConfig,
}
env = os.environ.get('ENV', '.dev')

config: Type[Config] = config_mappings[env]
