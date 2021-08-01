import os
import re
from logging import Logger
from jinja2 import FileSystemLoader
from jinja2 import Environment
from jinja2 import TemplatesNotFound
from mailmerge.infra.excepts.codes import ErrorCodesInfo
from mailmerge.infra.excepts.types import FilePathNotFound
from mailmerge.infra.excepts.types import FileContentNotExist
from mailmerge.infra.logging import scraping_logger
from mailmerge.infra.io.searchers import FilePathSearcher


class EmailDraftReader(object):
    _logger: Logger = scraping_logger

    def __init__(self, draftname: str):
        self._draftname = draftname
        self._draftpath: str = self._find_draftpath(draftname)

    def _find_draftpath(self, draftname: str) -> str:
        """
        找出檔案的路徑
        Args:
            draftname (str): 信件草稿名
        Raises:
            FilePathNotFound: 找不到該檔案路徑
        Returns:
            str: 檔案的完整路徑
        """
        if not FilePathSearcher.exist(draftname):
            raise FilePathNotFound(ErrorCodesInfo.EMAIL_DRAFT_PATH_NOT_EXIST, draftname)

        return FilePathSearcher.fullpath(draftname)

    def read(self) -> str:
        """
        讀取檔案的內容
        Returns:
            str: 讀取的內容文本
        """
        content: str = ""
        with open(self._draftpath, mode="r+", encoding="utf-8") as fp:
            content = fp.read()
        return content

    @property
    def draftpath(self) -> str:
        return self._draftpath
