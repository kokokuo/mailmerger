import pytest
from logging import Logger
from unittest.mock import MagicMock
from typing import Dict, List, Callable, Any
from domain.models.excel import ExcelSheetParser
from infra.excepts.codes import ErrorCodesInfo
from infra.excepts.types import SourceFilePathNotFound
from infra.excepts.types import SourceFileFormatError
from infra.excepts.types import SourceContentNotExist
from tests.config import TestConifg


class TestExcelSheetParser(object):

    @pytest.mark.parametrize("exist_sheet_filename", [
        TestConifg.TEST01_EN_HEADER_SHEET_FILENAME,
        TestConifg.TEST02_CN_HEADER_SHEET_FILENAME
    ])
    def test_file_is_excel_format_and_exist(self,
                                            exist_sheet_filename: str,
                                            logger: Logger,
                                            find_filename_path: Callable[[str], str]):
        exist_filepath: str = find_filename_path(exist_sheet_filename)
        self.excel = ExcelSheetParser(logger, exist_filepath)
        logger.debug(f"檔案路徑名稱 : {exist_filepath}")
        assert self.excel.filename == exist_filepath

    def test_file_not_found(self,
                            logger: Logger,
                            find_filename_path: Callable[[str], str]) -> None:
        non_exist_filename = TestConifg.TEST03_NON_EXIST_SHEET_FILENAME
        non_exist_filepath: str = find_filename_path(non_exist_filename)
        logger.debug(f"檔案路徑名稱 : {non_exist_filepath}")
        with pytest.raises(SourceFilePathNotFound) as errinfo:
            self.excel = ExcelSheetParser(logger, non_exist_filepath)
        logger.debug(f"Exception Info 資訊 : {errinfo.value}")
        assert errinfo.value.error_code == ErrorCodesInfo.EXCEL_NOT_FOUND.name

    def test_file_not_excel_format(self,
                                   logger: Logger,
                                   find_filename_path: Callable[[str], str]) -> None:
        non_excel_format_filename = TestConifg.TEST04_NON_EXCEL_FORMAT_FILE
        non_excel_format_filepath: str = find_filename_path(non_excel_format_filename)
        logger.debug(f"檔案路徑名稱 : {non_excel_format_filepath}")
        with pytest.raises(SourceFileFormatError) as errinfo:
            self.excel = ExcelSheetParser(logger, non_excel_format_filepath)
        logger.debug(f"Exception Info 資訊 : {errinfo.value}")
        assert errinfo.value.error_code is ErrorCodesInfo.FILE_NOT_EXCEL_FORMAT.name

    @pytest.mark.parametrize(
        "sheet_filename, expected",
        [
            (TestConifg.TEST01_EN_HEADER_SHEET_FILENAME, TestConifg.TEST01_EN_HEADER_SHEET_EXPECTED_RESULT),
            (TestConifg.TEST02_CN_HEADER_SHEET_FILENAME, TestConifg.TEST02_CN_HEADER_SHEET_EXPECTED_RESULT)
        ]
    )
    def test_read_default_sheet_data_correct(self,
                                             sheet_filename: str,
                                             expected: List[Dict[str, Any]],
                                             logger: Logger,
                                             find_filename_path: Callable[[str], str]) -> None:
        filepath: str = find_filename_path(sheet_filename)
        self.excel = ExcelSheetParser(logger, filepath)
        self.excel.read_sheet()
        sheet_records: List[Dict[str, Any]] = self.excel.sheet_data.to_dict("records")
        assert sheet_records == expected

    def test_read_default_sheet_data_not_correct(self,
                                                 logger: Logger,
                                                 find_filename_path: Callable[[str], str]) -> None:
        sheet_filename = TestConifg.TEST02_CN_HEADER_SHEET_FILENAME
        filepath: str = find_filename_path(sheet_filename)
        self.excel = ExcelSheetParser(logger, filepath)
        self.excel.read_sheet()
        sheet_records: List[Dict[str, Any]] = self.excel.sheet_data.to_dict("records")
        assert sheet_records is not TestConifg.TEST02_CN_HEADER_SHEET_NON_EXPECTED_RESULT

    # def test_read_sepcific_exist_sheetname(self,
    #                                        logger: Logger,
    #                                        find_filename_path: Callable[[str], str]) -> None:
    #     filename = TestConifg.TEST01_EN_HEADER_SHEET_FILENAME
    #     sheetname = TestConifg.TEST01_EN_HEADER_SHEET_NAME
    #     filepath: str = find_filename_path(filename)
    #     self.excel = ExcelSheetParser(logger, filename)
    #     self.excel.read_sheet(sheetname)

    def test_read_sepcific_non_exist_sheetname(self,
                                               logger: Logger,
                                               find_filename_path: Callable[[str], str]) -> None:
        filename = TestConifg.TEST01_EN_HEADER_SHEET_FILENAME
        sheetname = TestConifg.TEST01_EN_HEADER_NON_EXIST_SHEET_NAME
        filepath: str = find_filename_path(filename)
        self.excel = ExcelSheetParser(logger, filepath)

        with pytest.raises(SourceContentNotExist) as errinfo:
            self.excel.read_sheet(sheetname)
        assert errinfo.value.error_code is ErrorCodesInfo.SHEET_NOT_FOUND_IN_EXCEL.name
