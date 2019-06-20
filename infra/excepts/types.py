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


class SourceFilePathNotFound(ApplicationException):
    """
    來源檔案不存在
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str],
                 path: Optional[str] = None) -> None:
        self._path = path
        super(SourceFilePathNotFound, self).__init__(error, detail)

    @property
    def path(self) -> Optional[str]:
        return self._path


class SourceFileFormatError(ApplicationException):
    """
    來源檔案類型錯誤
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str],
                 path: Optional[str] = None) -> None:
        self._path = path
        super(SourceFileFormatError, self).__init__(error, detail)

    @property
    def path(self) -> Optional[str]:
        return self._path


class SourceContentNotExist(ApplicationException):
    """
    來源內容不存在（檔案存在但內容不在）
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 detail: Optional[str] = None) -> None:
        super(SourceContentNotExist, self).__init__(error, detail)
