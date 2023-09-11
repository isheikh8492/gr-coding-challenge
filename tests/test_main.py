import pytest
import filecmp
from main import parse_data


@pytest.mark.parametrize("input_file, expected_output_file", [
    ('tests/sample_input1.txt', 'tests/sample_input1_result.txt'),
    ('tests/sample_input2.txt', 'tests/sample_input2_result.txt'),
    ('tests/sample_input3.txt', 'tests/sample_input3_result.txt'),
    # add as many test cases as you want
])
def test_parse_data(input_file, expected_output_file):
    parse_data(input_file)




