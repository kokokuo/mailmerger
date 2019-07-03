import os
import re
from typing import List, Dict
from logging import Logger
from jinja2 import BaseLoader
from jinja2 import Environment, meta
from jinja2 import TemplatesNotFound
from apps.dto.source import ColHeader, RowSet
from infra.excepts.codes import ErrorCodesInfo
from infra.excepts.types import FilePathNotFound
from infra.logging import scraping_logger


class SourceMailMerger(object):
    # class level
    _logger = scraping_logger

    def __init__(self, draft_content: str) -> None:
        self._draft_content: str = draft_content
        self._find_pattern = r"{{2}[\w\u0020]*}{2}"
        self._sub_pattern = r"{{2}|}{2}"

    def merge_source(self,
                     headers: List[ColHeader],
                     dataset: List[Dict[ColHeader, RowSet]]) -> None:
        matched = re.findall(self._find_pattern, self._draft_content)
        if matched:
            for match_word in matched:
                header = re.sub(self._sub_pattern, "", match_word).strip()
                print(f"[ Matched ] header - {header}")
