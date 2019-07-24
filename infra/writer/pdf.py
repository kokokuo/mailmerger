# -*- coding: utf-8 -*-
import pdfkit
from . import IWriter


class PDFWriter(IWriter):
    @classmethod
    def write(cls, filename: str, src: str) -> bool:
        filename = filename + ".pdf"
        success = pdfkit.from_string(src, filename, options={'encoding': "UTF-8"})
        return success
