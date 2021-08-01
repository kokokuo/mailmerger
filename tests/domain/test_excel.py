import pytest
from logging import Logger
from unittest.mock import MagicMock
from typing import Dict, List, Callable, Any
from mailmerge.domain.models.sources import ExcelSheetParser
from mailmerge.infra.excepts.codes import ErrorCodesInfo
from mailmerge.infra.excepts.types import FilePathNotFound
from mailmerge.infra.excepts.types import FileFormatError
from mailmerge.infra.excepts.types import FileContentNotExist
from tests.config import TestSheetConfig, TestParsinExcelSheetConfig


@pytest.fixture(scope="function")
def cn_header_sheet_path(find_sheet_path: Callable[[str], str]):
    filename = TestSheetConfig.TEST_CN_HEADER_SHEET_FILENAME
    return find_sheet_path(filename)


class TestExcelSheetParser(object):
    def test_file_is_excel_format_and_exist(
        self, logger: Logger, find_sheet_path: Callable[[str], str]
    ):
        exist_sheet_filename = TestSheetConfig.TEST_CN_HEADER_SHEET_FILENAME
        exist_filepath: str = find_sheet_path(exist_sheet_filename)
        self.excel = ExcelSheetParser(exist_filepath)
        logger.debug(f"檔案路徑名稱 : {exist_filepath}")

        assert self.excel.filename == exist_filepath

    def test_file_not_exist(
        self, logger: Logger, find_sheet_path: Callable[[str], str]
    ) -> None:
        # Expected
        expected = ErrorCodesInfo.SOURCE_EXCEL_NOT_EXIST.name

        non_exist_filename = TestSheetConfig.TEST_NON_EXIST_SHEET_FILENAME
        non_exist_filepath: str = find_sheet_path(non_exist_filename)
        logger.debug(f"檔案路徑名稱 : {non_exist_filepath}")
        with pytest.raises(FilePathNotFound) as errinfo:
            self.excel = ExcelSheetParser(non_exist_filepath)
        logger.debug(f"Exception Info 資訊 : {errinfo.value}")

        assert errinfo.value.error_code == expected

    def test_file_not_excel_format(
        self, logger: Logger, find_sheet_path: Callable[[str], str]
    ) -> None:
        expected = ErrorCodesInfo.SOURCE_FILE_NOT_EXCEL_FORMAT.name

        non_excel_format_filename = TestSheetConfig.TEST_NON_EXCEL_FORMAT_FILE
        non_excel_format_filepath: str = find_sheet_path(non_excel_format_filename)
        logger.debug(f"檔案路徑名稱 : {non_excel_format_filepath}")
        with pytest.raises(FileFormatError) as errinfo:
            self.excel = ExcelSheetParser(non_excel_format_filepath)
        logger.debug(f"Exception Info 資訊 : {errinfo.value}")

        assert errinfo.value.error_code == expected

    @pytest.mark.parametrize(
        "sheet_filename, expected",
        [
            (
                TestSheetConfig.TEST_CN_HEADER_SHEET_FILENAME,
                TestParsinExcelSheetConfig.TEST_CN_HEADER_SHEET_EXPECTED_RESULT,
            ),
            (
                TestSheetConfig.TEST_EN_HEADER_SHEET_FILENAME,
                TestParsinExcelSheetConfig.TEST_EN_HEADER_SHEET_EXPECTED_RESULT,
            ),
        ],
    )
    def test_read_default_datasheet_correct(
        self,
        sheet_filename: str,
        expected: List[Dict[str, Any]],
        logger: Logger,
        find_sheet_path: Callable[[str], str],
    ) -> None:
        filepath: str = find_sheet_path(sheet_filename)
        self.excel = ExcelSheetParser(filepath)
        self.excel.read_sheet()
        sheet_records: List[Dict[str, Any]] = self.excel.datasheet.to_dict("records")

        assert sheet_records == expected

    def test_read_default_datasheet_data_not_correct(
        self, logger: Logger, find_sheet_path: Callable[[str], str]
    ) -> None:
        expected = (
            TestParsinExcelSheetConfig.TEST_CN_HEADER_SHEET_NON_EXPECTED_RESULT_DATA_DIFF
        )

        sheet_filename = TestSheetConfig.TEST_CN_HEADER_SHEET_FILENAME
        filepath: str = find_sheet_path(sheet_filename)
        self.excel = ExcelSheetParser(filepath)
        self.excel.read_sheet()
        sheet_records: List[Dict[str, Any]] = self.excel.datasheet.to_dict("records")

        assert sheet_records != expected

    def test_read_default_datasheet_order_not_correct(
        self, logger: Logger, find_sheet_path: Callable[[str], str]
    ) -> None:
        expected = (
            TestParsinExcelSheetConfig.TEST_CN_HEADER_SHEET_NON_EXPECTED_RESULT_ORDER_DIFF
        )

        sheet_filename = TestSheetConfig.TEST_CN_HEADER_SHEET_FILENAME
        filepath: str = find_sheet_path(sheet_filename)
        self.excel = ExcelSheetParser(filepath)
        self.excel.read_sheet()
        result: List[Dict[str, Any]] = self.excel.datasheet.to_dict("records")

        assert result != expected

    # 測試 Sheet 輸入指定是速表名稱有被執行到 -> Mock
    # def test_read_specific_exist_sheetname(self,
    #                                        logger: Logger,
    #                                        find_sheet_path: Callable[[str], str]) -> None:
    #     filename = TestSheetConfig.TEST_EN_HEADER_SHEET_FILENAME
    #     sheetname = TestSheetConfig.TEST_EN_HEADER_SHEET_NAME
    #     filepath: str = find_sheet_path(filename)
    #     self.excel = ExcelSheetParser(filename)
    #     self.excel.read_sheet(sheetname)

    def test_read_specific_non_exist_sheetname(
        self, logger: Logger, find_sheet_path: Callable[[str], str]
    ) -> None:
        expected = ErrorCodesInfo.SHEET_NOT_FOUND_IN_EXCEL.name

        filename = TestSheetConfig.TEST_EN_HEADER_SHEET_FILENAME
        sheetname = TestSheetConfig.TEST_EN_HEADER_NON_EXIST_SHEET_NAME
        filepath: str = find_sheet_path(filename)
        self.excel = ExcelSheetParser(filepath)

        with pytest.raises(FileContentNotExist) as errinfo:
            self.excel.read_sheet(sheetname)

        assert errinfo.value.error_code == expected
