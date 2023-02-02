# This code defines a Site class which has two class variables: source and dest, which are the paths to the source and destination directories respectively. 
# The class has a method called create_dir which takes a path argument, creates a new directory in the destination path based on the relative path of the input path to the source path. 
# It uses the mkdir method from the Path class to create the directory, with the parents and exist_ok arguments set to True, meaning that the method will create all necessary parent directories and not raise an error if the directory already exists. 
# The build method creates the destination directory if it does not exist and loops through all files and subdirectories in the source directory using the rglob method, creating directories using the create_dir method if it encounters a directory, and ignoring files for now.

from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source) # sets the source path to a Path object
        self.dest = Path(dest) # sets the destination path to a Path object
    
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source) # calculates the relative path from source to destination
        directory.mkdir(parents=True, exist_ok=True) # creates the directory in the destination path, creating parent directories if necessary
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True) # creates the destination directory if it does not exist
        for path in self.source.rglob("*"): # loops through all files and subdirectories in the source path
            if path.is_dir():
                self.create_dir(path) # creates a directory in the destination path if it encounters a directory in the source path
            else:
                pass # currently ignoring files
