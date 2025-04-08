import os


class FileSearcher:
    """Searches for files of a given size in a directory and its subdirectories."""

    def __init__(self, directory: str, file_size: int):
        self.directory = directory
        self.file_size = file_size
        self.matches = []

    def search_files(self):
        """Recursively searches for files of the specified size."""
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    if os.path.getsize(file_path) == self.file_size:
                        self.matches.append(file_path)
                except OSError:
                    pass  # Handle permission errors gracefully
        return self.matches
