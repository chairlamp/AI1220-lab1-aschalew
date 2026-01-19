# main.py
import json
import argparse
import src.file_io as io_mod
import src.gpt as gpt

def normalize_amount(extracted):
    """Normalize the amount field by stripping '$' and converting to float.

    Args:
        extracted (dict): Receipt data with an 'amount' field from the model.

    Returns:
        dict: Same mapping with 'amount' set to a float or None if unparseable.
    """
    amount = extracted.get("amount")
    if isinstance(amount, str):
        cleaned = amount.replace("$", "").strip()
        try:
            extracted["amount"] = float(cleaned)
        except ValueError:
            extracted["amount"] = None
    elif isinstance(amount, (int, float)):
        extracted["amount"] = float(amount)
    else:
        extracted["amount"] = None
    return extracted

def process_directory(dirpath):
    """Process all files in a directory and extract receipt info for each.

    Assumes the directory exists and contains readable receipt image files.
    Normalizes the extracted amount into a float where possible.

    Args:
        dirpath (str): Path to a directory containing receipt image files.

    Returns:
        dict: Mapping of filename to extracted receipt data dictionaries.
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        data = normalize_amount(data)
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
