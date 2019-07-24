import abc


class IWriter(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def write(cls, filename: str, src: str) -> bool:
        pass
