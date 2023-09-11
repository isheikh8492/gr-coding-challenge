# Car Rental Application Parser

## Project Overview

### Task Description

This application is responsible for logging a 'START' event when a rental car is picked up by the customer and an 'END' event when the car is returned. Each rental session is restricted to a 24-hour duration. The events are logged into an output file in the form of JSON records. This output file contains both 'START' and 'END' records for multiple rental sessions.

### Objectives

The primary objective of this project is to build a Python application that reads the output file and compiles a single summary record for each rental session, as specified in the project documentation.

---

## Setup and Running the Application

### Prerequisites

- Python 3.11
- PyCharm IDE (optional but recommended)
- pytest (for testing)

### Installation and Setup

1. **Clone the Repository**
   ```
   git clone https://github.com/username/gr-coding-challenge.git
   ```

2. **Navigate to the Project Directory**
   ```
   cd gr-coding-challenge
   ```

3. **Install Required Packages**
   ```
   pip install -r requirements.txt
   ```

### How to Run

1. **Execute the Main Application**
   ```
   python main.py
   ```

2. **Run Tests**
   To execute the tests, navigate to the root directory and run:
   ```
   python -m pytest
   ```

---

## Technical Details

### Approach

#### Algorithm and Data Structures

- The `json` library in Python is used to read JSON records from the file.
- A dictionary called `db` holds `Summary` objects keyed by a unique 'id'.
- The application iterates over the dictionary and uses Unix timestamps to generate summary records.
  
#### Handling Large Test Data

- A separate Python script (`synthetic_data_generation.py`) is available to generate a large set of test data (up to 100,000 entries).
- The dictionary-based storage allows for efficient lookup and update operations, making the application scalable for large datasets.

### Testing Strategy

- **Manual Test**: A manually created test file named `output_file_new.txt` is used for initial testing, and edge case testing.
- **Synthetic Test**: A programmatically generated file named `synthetic_output.txt` is used for performance.
  
All test files are located under different names in the `tests` folder. To run the test suite, execute `python -m pytest` in the root directory.

---

## Issues and Challenges

### Problems Faced

- The example output files initially caused confusion due to inconsistent 'id' and 'timestamp' formats.
- Timestamps in the 'END' records were sometimes incoherent or hard to interpret.

### Solutions and Workarounds

- Any inconsistencies were assumed to be errors. The IDs and timestamps were adjusted accordingly during processing.
- New test files were generated to cover a broad range of edge cases, ensuring the application’s robustness.

---

## Potential Improvements

- Possibility to store output data to a MySQL/SQLite3 database.

---

## Reflection

The project served as an excellent refresher for coding, problem-solving, and Python testing frameworks. The challenges encountered provided opportunities to revisit important programming and debugging techniques.
