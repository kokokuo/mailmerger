# -*- coding: utf-8 -*-
from typing import List
from logging import Logger
from infra.logging import scraping_logger
from apps.dto.source import PreMergeSourceDTO
from domain.models.sources import EmailDraftReader
from domain.models.merged import MergedSetVO
from domain.models.merged import OutputOption
from domain.models.merged import MergedOutputExcutor
from domain.models.merger import SourceMerger


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
        merger = SourceMerger(draft_content)
        merged_contents: List[MergedSetVO] = merger.merge_source(source.headers, source.dataset)
        results = MergedOutputExcutor.output(OutputOption.PDF, merged_contents)
        print(results)

    def merge2html(self, draft_content: str, source: PreMergeSourceDTO):
        pass

    def merge2send(self, draft_content: str, source: PreMergeSourceDTO):
        pass


merge_service = SourceMergeEmailDraftService()
