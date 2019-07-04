import os
from infra.excepts.types import FilePathNotFound
from infra.excepts.codes import ErrorCodesInfo


class FilePathSearcher(object):

    @classmethod
    def exist(cls, path: str) -> bool:
        """
        確認該路徑是否存在
        """
        if path.startswith("~"):
            fullpath = os.path.realpath(os.path.expanduser(path))
        else:
            fullpath = os.path.realpath(path)
        if os.path.exists(fullpath):
            return True
        return False

    @classmethod
    def fullpath(cls, path: str) -> str:
        """
        取得原路徑
        """
        if cls.exist(path):
            if path.startswith("~"):
                return os.path.realpath(os.path.expanduser(path))
            else:
                return os.path.realpath(path)
        raise FilePathNotFound(ErrorCodesInfo.PATH_NOT_FOUND, path)
