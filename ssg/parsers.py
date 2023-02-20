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
        # This method is not implemented and raises a NotImplementedError.
        # It is intended to parse a file at the given path and write the parsed output
        # to a new file at the given destination path.
        raise NotImplementedError
    
    def read(self, path):
        # This method reads the contents of a file at the given path and returns the contents as a string.
        # The file is opened in read mode using the open() function and the resulting file object is
        # automatically closed when the with block is exited. The contents of the file are read using
        # the read() method of the file object, and returned from the function.
        with open(path, 'r') as file:
            return file.read()
