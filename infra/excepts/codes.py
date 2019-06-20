# -*- coding: utf-8 -*-
from enum import Enum


class ErrorCodesInfo(Enum):
    """
    例外代碼與訊息
    """
    EXCEL_NOT_FOUND = "This path of excel file does not found."
    FILE_NOT_EXCEL_FORMAT = "This file does not belong to excel format type."
    SHEET_NOT_FOUND_IN_EXCEL = "This sheet does not exist in excel file."
    SHEET_CONTENT_EMPTY = "This content of sheet is empty, no data."
