# -*- coding: utf-8 -*-
import os
import importlib
from typing import Type, Union
from .base import Config
from .dev import DevConfig
from .prod import ProdConfig
"""
設定檔
"""


config_mappings = {
    ".dev": DevConfig,
    ".prod": ProdConfig,
}
env = os.environ.get('ENV', '.dev')

config: Type[Config] = config_mappings[env]
