# -*- coding: utf-8 -*-
from enum import Enum


class ErrorCodesInfo(Enum):
    """
    例外代碼與訊息
    """
    PATH_NOT_FOUND = "This path does not found."
    SOURCE_EXCEL_NOT_EXIST = "This path of source excel file does not exist."
    EMAIL_DRAFT_PATH_NOT_EXIST = "This path of email draft file does not exist."
    SOURCE_FILE_NOT_EXCEL_FORMAT = "This source file does not belong to excel format type."
    SHEET_NOT_FOUND_IN_EXCEL = "This sheet does not exist in excel file."
    SHEET_CONTENT_EMPTY = "This content of sheet is empty, no data."
    EMAIL_DRAFT_CONTENT_NOT_EXIST = "The content of email draft not exist, draft have not loaded yet"
    ALL_MERGE_TAG_NOT_MATCH = "The all tags of pre-defined for merging not matched"
    NO_MERGE_TAGS = 'There is no tags for merging in the draft.'
