# -*- coding: utf-8 -*-
from typing import List, Dict, Type
from collections import OrderedDict
from .dataset import MergedSetVO
from .option import OutputOption
from .result import OutputResultVO
from infra.writer import IWriter
from infra.writer.pdf import PDFWriter
from infra.writer.html import HtmlWriter


class MergedOutputExcutor(object):

    output_options: Dict[OutputOption, Type[IWriter]] = {
        OutputOption.PDF: PDFWriter,
        OutputOption.HTML: HtmlWriter
    }

    @classmethod
    def output(cls, option: OutputOption, merged_sets: List[MergedSetVO]) -> List[OutputResultVO]:
        """
        藉由提供輸出選項以及合併好的資料集來輸出資料集，
        Args:
            option (MergedOutputType): 輸出的選項 (HTML, PDF, EMAIL_SEND)
            merged_sets (List[MergedSetVO]): [description]

        Returns:
            List[OutputResultVO]: 輸出的結果集
        """
        dataset: MergedSetVO
        results: List[OutputResultVO] = []
        for dataset in merged_sets:
            success = cls.output_options[option].write(dataset.name, dataset.content)
            results.append(OutputResultVO(dataset.name, success))
        return results
