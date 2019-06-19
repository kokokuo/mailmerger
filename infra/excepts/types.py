# -*- coding: utf-8 -*-
from typing import Optional
from .codes import ErrorCodesInfo


class ApplicationException(Exception):
    def __init__(self, error: ErrorCodesInfo, detail: Optional[str]) -> None:
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


class SheetSourcePathNotFound(ApplicationException):
    """
    Sheet 來源不存在
    """
    def __init__(self,
                 error: ErrorCodesInfo,
                 path: str,
                 detail: Optional[str]) -> None:
        self._path = path
        super(SheetSourcePathNotFound, self).__init__(error, detail)

    @property
    def path(self) -> str:
        return self._path
