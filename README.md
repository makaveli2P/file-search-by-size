# File Search by Size

## Problem Statement

Given a directory path and a target file size (in bytes), this tool searches all files within that directory and its subdirectories and returns the paths of files whose size exactly matches the specified value.

## How to Run

### 1. Clone the Repository and navigate to it 

```bash
git clone https://github.com/makaveli2P/file-search-by-size.git
cd file-search-by-size
```

### 2. Run the Program

```bash
python main.py <directory_path> <file_size_in_bytes>
```

## Directory Structure
```
file-search-by-size/
├── main.py                # Entry point
├── file_system_search.py  # Controller that coordinates the search
├── file_searcher.py       # Contains logic for searching files by size
└── directory_scanner.py   # Handles directory validation and error checking
```
