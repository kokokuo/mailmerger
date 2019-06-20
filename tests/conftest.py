import os
import pytest
import logging
from logging import Logger
from .config import TestConifg
from typing import Callable


@pytest.fixture(scope="session")
def logger() -> Logger:
    name = TestConifg.LOGGER_NAME
    return logging.getLogger(name)


# @pytest.fixture(scope="session",
#                 params=[TestConifg.TEST01_EN_HEADER_SHEET_FILENAME, TestConifg.TEST02_CN_HEADER_SHEET_FILENAME])
# def sheet_filepath(logger: Logger, request) -> str:
#     filename = request.param
#     dirpath = os.path.dirname(__file__)
#     filepath = os.path.join(dirpath, filename)
#     logger.debug(f"檔案名稱：{filename} | 檔案路徑 : {filepath}")
#     return filepath


@pytest.fixture
def find_filename_path() -> Callable[[str], str]:
    """
    建立 pytest 的 Factories as fixtures ，使之能夠在其他測試方法中調用此 Fixture 方法傳遞資料
    Returns:
        func: 回傳方法
    """
    def _find_filename_path(filename: str) -> str:
        dirpath = os.path.dirname(__file__)
        sheet_dir = TestConifg.SHEET_TEST_DIRNAME
        filepath = os.path.join(dirpath, sheet_dir, filename)
        return filepath

    return _find_filename_path
