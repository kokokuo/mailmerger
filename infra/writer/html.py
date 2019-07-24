from . import IWriter


class HtmlWriter(IWriter):
    @classmethod
    def write(cls, filename: str, src: str) -> bool:
        filename = filename + ".html"
        try:
            with open(filename, "r+", encoding="utf8") as fp:
                fp.write(src)
            return True
        except Exception as e:
            return False
