# -*- coding: utf-8 -*-
import os
from typing import Optional
from logging import Logger
import pandas as pd
from infra.excepts.types import SourceFilePathNotFound
from infra.excepts.types import SourceFileFormatError
from infra.excepts.types import SourceContentNotExist
from infra.excepts.codes import ErrorCodesInfo


class ExcelSheetParser(object):
    def __init__(self, filename: str):
        self._set_filename(filename)
        self._sheet_data: pd.DataFrame = pd.DataFrame()

    def _does_excel_format(self, path: str) -> bool:
        support_extension = ['.xlsx', '.xls']
        for extension in support_extension:
            if path.endswith(extension):
                return True
        return False

    def _set_filename(self, filename: str) -> None:
        if not os.path.exists(filename):
            raise SourceFilePathNotFound(ErrorCodesInfo.EXCEL_NOT_FOUND, filename)
        if not self._does_excel_format(filename):
            raise SourceFileFormatError(ErrorCodesInfo.FILE_NOT_EXCEL_FORMAT, filename)

        self._filename = filename

    @property
    def sheet_data(self) -> pd.DataFrame:
        return self._sheet_data

    @property
    def filename(self) -> str:
        return self._filename

    def read_sheet(self, sheetname: Optional[str] = None) -> None:
        """
        讀取 Sheet 內容並且抓取資料
        Args:
            sheetname (Optinoal[str]): 要讀取的 Sheet 檔案。若為輸入，預設為第一張 Sheet
        """
        excel = pd.ExcelFile(self._filename)
        if sheetname:
            if sheetname not in excel.sheet_names:
                raise SourceContentNotExist(ErrorCodesInfo.SHEET_NOT_FOUND_IN_EXCEL)
            self._sheet_data = excel.parse(self._filename, sheetname)
        else:
            self._sheet_data = excel.parse(self._filename)

    # def read_sheets(self) -> None:
    #     """
    #     讀取所有的 Sheets 內容並抓取資料
    #     Args:
    #         sheetname (Optinoal[str]): 要讀取的 Sheet 檔案。若為輸入，預設為第一張 Sheet
    #     """
    #     pass
