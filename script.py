from catalog_suffix_fixer import process as p


def process(path: str) -> dict:
    result = p.process_file(file=path)
    return result
