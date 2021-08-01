

class OutputResultVO(object):
    """
    輸出的結果集
    args:
        name (str): 該資料集的名稱
        success (str): 輸出的結果
    """
    def __init__(self, name: str, success: bool):
        self._name = name
        self._success = success

    @property
    def name(self) -> str:
        return self._name

    @property
    def success(self) -> bool:
        return self._success

    def __eq__(self, other: object):
        if not isinstance(other, OutputResultVO):
            return False
        if self.name == other.name and self.success == other.success:
            return True
        return False

    def __repr__(self):
        return "<OutputResultVO: name=%r, success=%r>" % (self.name, self.success)
