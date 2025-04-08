from directory_scanner import DirectoryScanner
from file_searcher import FileSearcher


class FileSystemSearch:
    """Handles user input and orchestrates the file search process."""

    def __init__(self, directory: str, file_size: int):
        self.directory_scanner = DirectoryScanner(directory)
        self.file_searcher = FileSearcher(directory, file_size)

    def find_files(self):
        """Validates the directory and performs the search."""
        self.directory_scanner.validate_directory()
        return self.file_searcher.search_files()
