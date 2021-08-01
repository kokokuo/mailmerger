import pytest
from typing import Callable
from logging import Logger
from mailmerge.apps.dto.source import PreMergeSourceDTO
from mailmerge.apps.services.datasource import PreMergeSourceParsingService
from tests.config import TestSheetConfig, TestParsingSourceConfig


@pytest.fixture(scope="function")
def cn_header_sheet_path(find_sheet_path: Callable[[str], str]):
    filename = TestSheetConfig.TEST_CN_HEADER_SHEET_FILENAME
    return find_sheet_path(filename)


class TestPreMergeSourceParsingService(object):
    def test_parse_excel_result_correct(self, logger: Logger, cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_EXPECTED_COLHEADER,
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parse_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parse_excel 的結果 : {result_dto}")
        assert result_dto == expected

    def test_parse_excel_result_header_data_not_correct(self,
                                                          logger: Logger,
                                                          cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_DATA_DIFF,
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parse_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parse_excel 的結果 : {result_dto}")
        assert result_dto != expected

    def test_parse_excel_result_header_order_not_correct(self,
                                                           logger: Logger,
                                                           cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_ORDER_DIFF,
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parse_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parse_excel 的結果 : {result_dto}")
        assert result_dto != expected

    def test_parse_excel_result_row_data_not_correct(self,
                                                       logger: Logger,
                                                       cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_DATA_DIFF,
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parse_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parse_excel 的結果 : {result_dto}")
        assert result_dto != expected

    def test_parse_excel_result_row_order_not_correct(self,
                                                        logger: Logger,
                                                        cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_ORDER_DIFF,
            TestParsingSourceConfig.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parse_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parse_excel 的結果 : {result_dto}")
        assert result_dto != expected
