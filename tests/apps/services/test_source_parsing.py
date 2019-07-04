import pytest
from typing import Callable
from logging import Logger
from apps.dto.source import PreMergeSourceDTO
from apps.services.datasource import PreMergeSourceParsingService
from tests.config import TestSheetConifg, TestParsingSourceConifg


@pytest.fixture(scope="function")
def cn_header_sheet_path(find_sheet_path: Callable[[str], str]):
    filename = TestSheetConifg.TEST_CN_HEADER_SHEET_FILENAME
    return find_sheet_path(filename)


class TestPreMergeSourceParsingService(object):
    def test_parsing_excel_result_correct(self, logger: Logger, cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_EXPECTED_COLHEADER,
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parsing_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parsing_excel 的結果 : {result_dto}")
        assert result_dto == expected

    def test_parsing_excel_result_header_data_not_correct(self,
                                                          logger: Logger,
                                                          cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_DATA_DIFF,
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parsing_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parsing_excel 的結果 : {result_dto}")
        assert result_dto != expected

    def test_parsing_excel_result_header_order_not_correct(self,
                                                           logger: Logger,
                                                           cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_ORDER_DIFF,
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parsing_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parsing_excel 的結果 : {result_dto}")
        assert result_dto != expected

    def test_parsing_excel_result_row_data_not_correct(self,
                                                       logger: Logger,
                                                       cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_DATA_DIFF,
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parsing_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parsing_excel 的結果 : {result_dto}")
        assert result_dto != expected

    def test_parsing_excel_result_row_order_not_correct(self,
                                                        logger: Logger,
                                                        cn_header_sheet_path: str) -> None:

        expected = PreMergeSourceDTO(
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_ORDER_DIFF,
            TestParsingSourceConifg.TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET
        )

        service = PreMergeSourceParsingService()
        result_dto: PreMergeSourceDTO = service.parsing_excel(cn_header_sheet_path)
        logger.debug(f"PreMergeSourceParsingService 執行 parsing_excel 的結果 : {result_dto}")
        assert result_dto != expected
