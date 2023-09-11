import pytest
import csv
from main import parse_data


@pytest.mark.parametrize("input_file", [
    'tests/sample_input1.txt',
    'tests/sample_input2.txt',
    # add more file paths here as needed
])
def test_sorted_timestamp(input_file):
    output_file_name = parse_data(input_file)

    with open(output_file_name, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            id = line.split('\t\t')[0]
            try:
                summary_start_time = int(line.split('\t\t')[1])
                summary_end_time = int(line.split('\t\t')[2])
            except ValueError:
                assert False, f"Failed to parse start or end time for session {id} as integers"

            assert summary_end_time >= summary_start_time, f"End time of {id} is less than start time"
