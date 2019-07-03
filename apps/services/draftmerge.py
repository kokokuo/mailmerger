# -*- coding: utf-8 -*-
from logging import Logger
from infra.logging import scraping_logger
from apps.dto.source import PreMergeSourceDTO
from domain.models.draft import EmailDraftReader
from domain.models.merger import SourceMailMerger


class SourceMergeEmailDraftService(object):
    # class level
    _logger: Logger = scraping_logger

    def __init__(self) -> None:
        pass

    def read_draft(self, filename: str) -> str:
        """
        讀取信件草稿的檔案內容
        Args:
            filename (str): 信件檔案來源名稱
        Returns:
            str: 讀取的內容文本
        """
        reader = EmailDraftReader(filename)
        return reader.read()

    def merge2pdf(self, draft_content: str, source: PreMergeSourceDTO):
        pass

    def merge2html(self, draft_content: str, source: PreMergeSourceDTO):
        merger = SourceMailMerger(draft_content)
        merger.merge_source(source.headers, source.dataset)

    def merge2send(self, draft_content: str, source: PreMergeSourceDTO):
        pass


merge_service = SourceMergeEmailDraftService()