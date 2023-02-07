from pathlib import Path
from typing import List

class Parser:
    extensions : List[str] = []
    def valid_extension(self,extension):
        if extension == self.extenstions.rglob("*"):
            return True
        else:
            pass