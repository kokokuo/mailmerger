# -*- coding: utf-8 -*-
from typing import Optional
from .codes import ErrorCodesInfo


class ApplicationException(Exception):
    def __init__(self, error: ErrorCodesInfo, detail: Optional[str] = None) -> None:
        self._error_code = error.name
        self._error_message = error.value
        self._detail = detail

    @property
    def error_code(self) -> str:
        return self._error_code

    @property
    def error_message(self) -> str:
        return self._error_message

    @property
    def detail(self) -> Optional[str]:
        return self._detail


class FilePathNotFound(ApplicationException):
    """
    來源檔案不存在
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str],
                 path: Optional[str] = None) -> None:
        self._path = path
        super(FilePathNotFound, self).__init__(error, detail)

    @property
    def path(self) -> Optional[str]:
        return self._path


class FileFormatError(ApplicationException):
    """
    來源檔案類型錯誤
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str],
                 path: Optional[str] = None) -> None:
        self._path = path
        super(FileFormatError, self).__init__(error, detail)

    @property
    def path(self) -> Optional[str]:
        return self._path


class FileContentNotExist(ApplicationException):
    """
    來源內容不存在（檔案存在但內容不在）
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str] = None) -> None:
        super(FileContentNotExist, self).__init__(error, detail)


class MergedContentFailed(ApplicationException):
    """
    合併內容失敗
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str] = None) -> None:
        super(MergedContentFailed, self).__init__(error, detail)
