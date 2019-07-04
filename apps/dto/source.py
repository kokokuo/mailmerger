from typing import List, Dict, NewType, Any


ColHeader = str
RowSet = Any


class PreMergeSourceDTO(object):
    def __init__(self,
                 headers: List[ColHeader],
                 dataset: List[Dict[ColHeader, RowSet]]) -> None:
        self.headers = headers
        self.dataset = dataset

    def __eq__(self, other) -> bool:
        if isinstance(other, PreMergeSourceDTO):
            if self.headers == other.headers and self.dataset == other.dataset:
                return True
        return False

    def __repr__(self):
        return f"<PreMergeSourceDTO ========== \n\
                  - headers: {self.headers} \n\
                   -dataset: {self.dataset} \n\
                  ========================================>"
