import re
from typing import IO
from catalog_suffix_fixer.functions import parsing as parse
from pandas import DataFrame


def process(df: DataFrame, file_out: str) -> dict:
    if not parse.verify_format(df):
        return {"ERROR": "File not in required format."}
    df = parse.sort_df(df)
    df = parse.remove_empty_rows(df)
    processed_count = parse.number_processed(df)
    df = parse.generate_new_records(df)
    generated_count = parse.number_generated(df, processed_count)
    new_total_count = processed_count + generated_count
    # check if file exists in output
    # file_out = re.sub(r"\..*$", "_processed.tsv", name)
    parse.save_df(df, file_out)
    return {
        "records_in": processed_count,
        "records_out": new_total_count,
        "records_generated": generated_count,
    }


def process_file(file, output: str) -> dict:
    # do a thing
    df = parse.import_data_file(file)
    return process(df, file_out=output)


def process_local(file: str, output: str) -> dict:
    # do a thing
    df = parse.import_data(file)
    return process(df, file_out=output)
