import os


class DirectoryScanner:
    """Validates a directory path before searching."""

    def __init__(self, directory: str):
        self.directory = directory

    def validate_directory(self):
        """Checks if the directory exists and is accessible."""
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Directory not found: {self.directory}")
        if not os.path.isdir(self.directory):
            raise NotADirectoryError(f"Path is not a directory: {self.directory}")
        return True
