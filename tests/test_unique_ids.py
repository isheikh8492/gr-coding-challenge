import pytest
import csv
from main import parse_data


@pytest.mark.parametrize("input_file", [
    'tests/sample_input1.txt',
    'tests/sample_input2.txt',
    # add more file paths here as needed
    'tests/sample_input3.txt',
])
def test_unique_ids(input_file):
    output_file_name = parse_data(input_file)
    unique_ids = set()

    with open(output_file_name, 'r') as file:
        lines = file.readlines()[1:]

        for line in lines:
            summary_id = line.split('\t\t')[0]
            assert summary_id not in unique_ids, f"Duplicate ID found: {summary_id}"
            unique_ids.add(summary_id)
