# -*- coding: utf-8 -*-


class MergedSetVO(object):
    """
    合併後的資料集
    Agrs:
        name (str): 該資料集的名稱
        content (str): 合併後的內容
    """
    def __init__(self, name: str, content: str):
        self._name = name
        self._content = content

    @property
    def name(self) -> str:
        return self._name

    @property
    def content(self) -> str:
        return self._content

    def __eq__(self, other: object):
        if not isinstance(other, MergedSetVO):
            return False
        if self.name == other.name and self.content == other.content:
            return True
        return False

    def __repr__(self):
        return "<MergedSetVO: name=%r, content=%r>" % (self.name, self.content)
