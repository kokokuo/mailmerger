import os
import re
import copy
from typing import List, Dict
from collections import OrderedDict
from logging import Logger
from jinja2 import BaseLoader
from jinja2 import Environment, meta
from jinja2 import TemplatesNotFound
from mailmerge.apps.dto.source import ColHeader, RowSet
from mailmerge.domain.models.merged import MergedSetVO
from mailmerge.infra.excepts.codes import ErrorCodesInfo
from mailmerge.infra.excepts.types import MergedContentFailed
from mailmerge.infra.logging import scraping_logger
import pdfkit


class SourceMerger(object):
    # class level
    _logger = scraping_logger

    def __init__(self, draft_content: str) -> None:
        self._draft_content: str = draft_content
        self._find_pattern = r"{{2}[\w\u0020]*}{2}"
        self._sub_pattern = r"{{2}|}{2}"

    def _clean_word(self, word: str):
        return re.sub(self._sub_pattern, "", word).strip()

    def _merge_rowset(self,
                      src_headers: List[ColHeader],
                      src_dataset: Dict[ColHeader, RowSet],
                      found_words: List[str]) -> str:
        """
        合併每一列的資料集到信件草稿
        Args:
            src_headers (List[ColHeader]): 資料來源的所有標頭欄位表
            src_dataset (Dict[ColHeader, RowSet]): 該列的資料來源集合
            found_words (List[str]): 與草稿找到的符合規則關鍵詞

        Raises:
            MergedContentFailed: 若有符合的標籤，但都沒有匹配到對應的關鍵字詞，則回報 ALL_MERGE_TAG_NOT_MATCH

        Returns:
            str: 合併好的內榮
        """
        merge_content: str = copy.deepcopy(self._draft_content)
        matched_headers = [
            self._clean_word(found_word)
            for found_word in found_words
            if self._clean_word(found_word) in src_headers
        ]
        if not matched_headers:
            raise MergedContentFailed(ErrorCodesInfo.ALL_MERGE_TAG_NOT_MATCH)

        for header in matched_headers:
            merged_pattern = r"{{2}[\u0020]*" + header + r"[\u0020]*}{2}"
            self._logger.debug(f"[ Matched ] header - {header}")
            source_content = src_dataset[header]
            merge_content = re.sub(merged_pattern, source_content, merge_content)
        return merge_content

    def merge_source(self,
                     src_headers: List[ColHeader],
                     src_datasets: List[Dict[ColHeader, RowSet]]) -> List[MergedSetVO]:
        """
        合併資料來源到信件草稿
        Args:
            src_headers (List[ColHeader]): 來源的資料標頭欄位
            src_datasets (List[Dict[ColHeader, RowSet]]): 來源的資料列

        Raises:
            MergedContentFailed: 若沒有符合的合併標籤，則回報 NO_MERGE_TAGS 例外

        Returns:
            List[MergedSetVO]: 合併完的資料集
        """
        ROWSET_NAME_IDX = 0
        found_words = re.findall(self._find_pattern, self._draft_content)
        merged_contents: List[MergedSetVO] = []
        if found_words:
            for dataset in src_datasets:
                merged_name = dataset[src_headers[ROWSET_NAME_IDX]]
                merged_content = self._merge_rowset(src_headers, dataset, found_words)
                merged_contents.append(MergedSetVO(merged_name, merged_content))
            return merged_contents
        raise MergedContentFailed(ErrorCodesInfo.NO_MERGE_TAGS)
