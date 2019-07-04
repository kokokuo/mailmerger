from typing import List, Dict
from pandas import DataFrame
from apps.dto.source import PreMergeSourceDTO, ColHeader, RowSet


class PreMergeSourceAssembler(object):

    def sheet2source(self, datasheet: DataFrame) -> PreMergeSourceDTO:
        headers: List[ColHeader] = list(datasheet.columns.values)
        # Convert to dict of list data
        datasets: List[Dict[ColHeader, RowSet]] = datasheet.to_dict("recrods")
        return PreMergeSourceDTO(headers, datasets)
