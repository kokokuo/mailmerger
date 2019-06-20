import pytest
from typing import Callable
from logging import Logger
from unittest.mock import MagicMock
from domain.models.excel import ExcelSheetParser
from infra.excepts.codes import ErrorCodesInfo
from infra.excepts.types import SourceFilePathNotFound
from infra.excepts.types import SourceFileFormatError
from infra.excepts.types import SourceContentNotExist
from tests.config import TestConifg


class TestExcelSheetParser(object):

    @pytest.mark.parametrize("exist_sheet_filename", [
        TestConifg.TEST01_SHEET_SOURCE,
        TestConifg.TEST02_SHEET_SOURCE
    ])
    def test_file_is_excel_format_and_exist(self,
                                            logger: Logger,
                                            exist_sheet_filename: str,
                                            find_filename_path: Callable[[str], str]):
        exist_filepath: str = find_filename_path(exist_sheet_filename)
        self.excel = ExcelSheetParser(exist_filepath)
        logger.debug(f"檔案路徑名稱 : {exist_filepath}")
        assert self.excel.filename == exist_filepath

    def test_file_not_found(self,
                            logger: Logger,
                            find_filename_path: Callable[[str], str]) -> None:
        non_exist_filename = TestConifg.NON_EXIST_SHEET_FILENAME
        non_exist_filepath: str = find_filename_path(non_exist_filename)
        logger.debug(f"檔案路徑名稱 : {non_exist_filepath}")
        with pytest.raises(SourceFilePathNotFound) as errinfo:
            self.excel = ExcelSheetParser(non_exist_filepath)
        logger.debug(f"Exception Info 資訊 : {errinfo.value}")
        assert errinfo.value.error_code is ErrorCodesInfo.EXCEL_NOT_FOUND.name

    def test_file_not_excel_format(self,
                                   logger: Logger,
                                   find_filename_path: Callable[[str], str]) -> None:
        non_excel_format_filename = TestConifg.NON_EXCEL_FORMAT_FILE
        non_excel_format_filepath: str = find_filename_path(non_excel_format_filename)
        logger.debug(f"檔案路徑名稱 : {non_excel_format_filepath}")
        with pytest.raises(SourceFileFormatError) as errinfo:
            self.excel = ExcelSheetParser(non_excel_format_filepath)
        logger.debug(f"Exception Info 資訊 : {errinfo.value}")
        assert errinfo.value.error_code is ErrorCodesInfo.FILE_NOT_EXCEL_FORMAT.name

    def test_read_sheet_and_data_correct(self,
                                         logger: Logger,
                                         find_filename_path: Callable[[str], str]) -> None:
        pass
