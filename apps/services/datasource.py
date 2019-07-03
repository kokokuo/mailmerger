# -*- coding: utf-8 -*-
from logging import Logger
from apps.dto.source import PreMergeSourceDTO
from apps.assembler.source import PreMergeSourceAssembler
from domain.models.excel import ExcelSheetParser
from infra.logging import scraping_logger


class PreMergeSourceParsingService(object):
    # class level
    _logger: Logger = scraping_logger

    def __init__(self) -> None:
        pass

    def parsing_excel(self, filename: str) -> PreMergeSourceDTO:
        self._excel = ExcelSheetParser(filename)
        self._excel.read_sheet()
        resp_dto = PreMergeSourceAssembler().sheet2source(self._excel.datasheet)
        self._logger.debug(f"轉換成 PreMergeSourceDTO 的資料格式 : {resp_dto}")
        return resp_dto


parsing_service = PreMergeSourceParsingService()