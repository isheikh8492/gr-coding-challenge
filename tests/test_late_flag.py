import pytest
import csv
import ast
from main import parse_data


@pytest.mark.parametrize("input_file", [
    'tests/sample_input1.txt',
    'tests/sample_input2.txt',
    # add more file paths here as needed
    'tests/sample_input3.txt',
])
def test_late_flag(input_file):
    output_file_name = parse_data(input_file)

    with open(output_file_name, 'r') as file:
        lines = file.readlines()[1:]

        for line in lines:
            summary = line.split('\t\t')
            duration_hr = (int(summary[2]) - int(summary[1])) / 3600
            assert (duration_hr > 24) == (ast.literal_eval(summary[4])), f"Late flag doesn't reflect duration limit " \
                                                                         f"crossing"
