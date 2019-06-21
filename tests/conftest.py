import os
import pytest
import logging
from logging import Logger
from .config import TestCommonConifg
from typing import Callable


@pytest.fixture(scope="session")
def logger() -> Logger:
    name = TestCommonConifg.LOGGER_NAME
    return logging.getLogger(name)


# @pytest.fixture(scope="session",
#                 params=[TestCommonConifg.TEST_EN_HEADER_SHEET_FILENAME, TestCommonConifg.TEST_CN_HEADER_SHEET_FILENAME])
# def sheet_filepath(logger: Logger, request) -> str:
#     filename = request.param
#     dirpath = os.path.dirname(__file__)
#     filepath = os.path.join(dirpath, filename)
#     logger.debug(f"檔案名稱：{filename} | 檔案路徑 : {filepath}")
#     return filepath


@pytest.fixture
def find_sheet_path() -> Callable[[str], str]:
    """
    建立 pytest 的 Factories as fixtures ，使之能夠在其他測試方法中調用此 Fixture 方法傳遞資料
    Returns:
        func: 回傳方法
    """
    def _find_sheet_path(filename: str) -> str:
        dirpath = os.path.dirname(__file__)
        sheet_dir = TestCommonConifg.SHEET_TEST_DIRNAME
        filepath = os.path.join(dirpath, sheet_dir, filename)
        return filepath

    return _find_sheet_path


@pytest.fixture
def find_email_template_path() -> Callable[[str], str]:
    """
    建立 pytest 的 Factories as fixtures ，使之能夠在其他測試方法中調用此 Fixture 方法傳遞資料
    Returns:
        func: 回傳方法
    """
    def _find_email_template_path(filename: str) -> str:
        dirpath = os.path.dirname(__file__)
        email_dir = TestCommonConifg.EMAIL_TEMPLATE_TEST_DIRNAME
        filepath = os.path.join(dirpath, email_dir, filename)
        return filepath

    return _find_email_template_path
