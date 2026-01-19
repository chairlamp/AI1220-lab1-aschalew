# main.py
import json
import argparse
import src.file_io as io_mod
import src.gpt as gpt

def process_directory(dirpath):
    """Process all files in a directory and extract receipt info for each.

    Assumes the directory exists and contains readable receipt image files.

    Args:
        dirpath (str): Path to a directory containing receipt image files.

    Returns:
        dict: Mapping of filename to extracted receipt data dictionaries.
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        results[name] = data
    return results

def main():
    """Parse CLI arguments, process the directory, and optionally print JSON.

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
