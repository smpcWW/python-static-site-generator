from pathlib import Path
from typing import List

class Parser:
    # Class variable to store the list of extensions
    extensions : List[str] = []
    
    def valid_extension(self,extension):
        """
        Method to check if the given extension is in the class variable 'extensions'
        
        Args:
            extension (str): The extension to check for validity
        
        Returns:
            bool: True if the given extension is in the class variable 'extensions', False otherwise
        """
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(self, path):
        with open(path, 'r') as file:
            contents = file.read()
            return contents