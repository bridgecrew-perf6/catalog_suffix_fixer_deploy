from catalog_suffix_fixer import process as p

myfile = (
    "catalog_suffix_fixer/Import Copy of History Catalog Data Entry H19235 to 22925.csv"
)


def main(path: str) -> dict:
    result = p.process_file(file=path)
    return result


# if __name__ == "__main__":
#     result = main(myfile)
#     print(result)
