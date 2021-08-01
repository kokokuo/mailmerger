# -*- coding: utf-8 -*-
import os
from typing import Optional
from logging import Logger
import pandas as pd
from mailmerge.infra.logging import scraping_logger
from mailmerge.infra.excepts.types import FilePathNotFound
from mailmerge.infra.excepts.types import FileFormatError
from mailmerge.infra.excepts.types import FileContentNotExist
from mailmerge.infra.excepts.codes import ErrorCodesInfo
from mailmerge.infra.io.searchers import FilePathSearcher


class ExcelSheetParser(object):
    # class level
    _logger = scraping_logger

    def __init__(self, filename: str):
        self._set_filename(filename)
        self._datasheet: pd.DataFrame = pd.DataFrame()
        self._excel = pd.ExcelFile(self.filename)

    def _does_excel_format(self, path: str) -> bool:
        support_extension = ['.xlsx', '.xls']
        for extension in support_extension:
            if path.endswith(extension):
                return True
        return False

    def _set_filename(self, filename: str) -> None:
        if not FilePathSearcher.exist(filename):
            raise FilePathNotFound(ErrorCodesInfo.SOURCE_EXCEL_NOT_EXIST, filename)
        if not self._does_excel_format(filename):
            raise FileFormatError(ErrorCodesInfo.SOURCE_FILE_NOT_EXCEL_FORMAT, filename)

        self._filename = FilePathSearcher.fullpath(filename)

    @property
    def datasheet(self) -> pd.DataFrame:
        return self._datasheet

    @property
    def filename(self) -> str:
        return self._filename

    def read_sheet(self, sheetname: Optional[str] = None) -> None:
        """
        讀取 Sheet 內容並且抓取資料
        Args:
            sheetname (Optinoal[str]): 要讀取的 Sheet 檔案。若為輸入，預設為第一張 Sheet
        """

        if sheetname:
            if sheetname not in self._excel.sheet_names:
                raise FileContentNotExist(ErrorCodesInfo.SHEET_NOT_FOUND_IN_EXCEL)
            self._datasheet = self._excel.parse(sheetname)
        else:
            self._datasheet = self._excel.parse()

    # def read_sheets(self) -> None:
    #     """
    #     讀取所有的 Sheets 內容並抓取資料
    #     Args:
    #         sheetname (Optinoal[str]): 要讀取的 Sheet 檔案。若為輸入，預設為第一張 Sheet
    #     """
    #     pass
