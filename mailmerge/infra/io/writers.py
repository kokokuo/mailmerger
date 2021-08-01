import abc
import pdfkit


class IWriter(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def write(cls, filename: str, src: str) -> bool:
        pass


class HtmlWriter(IWriter):
    @classmethod
    def write(cls, filename: str, src: str) -> bool:
        filename = filename + ".html"
        try:
            with open(filename, "w+", encoding="utf8") as fp:
                fp.write(src)
            return True
        except Exception as e:
            return False


class PDFWriter(IWriter):
    @classmethod
    def write(cls, filename: str, src: str) -> bool:
        filename = filename + ".pdf"
        success = pdfkit.from_string(src, filename, options={'encoding': "UTF-8"})
        return success
