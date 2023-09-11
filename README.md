# Car Rental Application Parser

## Project Overview

### Task Description
This application is designed to log a 'START' event when a rental car is picked up by the customer and an 'END' event when the car is returned. Each rental session is limited to 24 hours. These events are recorded in an output file as JSON records. The output file contains 'START' and 'END' records for multiple rental sessions.

### Objectives
The objective is to develop a Python application that parses the output file and generates a single summary record for each rental session as prescribed in the project documentation.

---

## Setup and Running the Application

### Requirements
- Python 3.11
- PyCharm IDE (optional)
- pytest (for testing)

### Installation

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/isheikh8492/gr-coding-challenge.git
   ```

2. Navigate to the project directory.
   ```
   cd gr-coding-challenge
   ```

3. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```

### How to Run

Run the `main.py` script to execute the application.
```
python main.py
```

To run tests, navigate to the root directory of the project and run:
```
python -m pytest
```

---

## Technical Details

### Approach

#### Algorithm and Data Structures
- The application uses Python's built-in `json` library for parsing JSON records.
- Utilizes a dictionary called 'db' to store 'Summary' objects, keyed by 'id'.
- Main logic uses iteration and Unix timestamps to create summary records.

### Testing Strategy

- Manual tests: `output_file_new.txt`
- Synthetic tests: `synthetic_output.txt`

Tests can be found in the `tests` folder. To run all tests, execute `python -m pytest`.

---

## Issues and Challenges

- Inconsistencies in example output files led to initial confusion.
- Timestamps in the 'END' records were not always coherent or easily understandable.

### Solutions and Workarounds

- Assumed erroneous placement of timestamps and adjusted IDs accordingly.
- Generated new test files to cover various edge cases.

---

## Potential Improvements

- Possibility to store output data to a MySQL/SQLite3 database.
  
---

## Reflection

The project served as an excellent refresher for coding, problem-solving, and Python testing frameworks. The challenges encountered provided opportunities to revisit important programming and debugging techniques.
