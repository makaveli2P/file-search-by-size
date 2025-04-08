import argparse
from file_system_search import FileSystemSearch

def main():
    parser = argparse.ArgumentParser(description="Search for files of a specific size.")
    parser.add_argument("directory", type=str, help="The directory to search.")
    parser.add_argument("size", type=int, help="File size in bytes to match.")

    args = parser.parse_args()

    search_tool = FileSystemSearch(args.directory, args.size)
    results = search_tool.find_files()

    if results:
        print("Files found:")
        for file in results:
            print(file)
    else:
        print("No files found matching the criteria.")

if __name__ == "__main__":
    main()
