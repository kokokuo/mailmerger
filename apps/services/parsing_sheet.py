# -*- coding: utf-8 -*-
from logging import Logger
from infra.logging import scraping_logger
import pandas as pd


class SheetsParsingService(object):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def parsing_excel(self, filename: str) -> None:
        pass

