import os

from .csv import CsvParser
from .json import JsonParser
from .xml import XmlParser


class ParserFactory:
    @staticmethod
    def get_parser(file_path):
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        if ext == ".csv":
            return CsvParser()
        elif ext == ".json":
            return JsonParser()
        elif ext == ".xml":
            return XmlParser()
        else:
            raise ValueError(f"Unsupported file type: {ext}")
