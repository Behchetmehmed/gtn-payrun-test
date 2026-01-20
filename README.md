# GTN → Payrun Mapping Unit Tests

## Overview
This project contains unit tests to verify that customer payroll data (GTN files) is correctly mapped to the Payslip format (Payrun files).

- `test_payrun_mapping.py`: contains all unit tests.
- `Files`: folders with test files (GTN.xlsx, Payrun.xlsx, mapping.json).

## Test Cases

1. **File type** – Checks if GTN and Payrun files are `.xlsx`.
2. **Empty rows** – Checks if GTN file has empty lines.
3. **Header structure** – Checks if GTN file has the correct number of header rows.
4. **Employees missing in GTN** – Checks if employees in Payrun are also in GTN.
5. **Employees missing in Payrun** – Checks if employees in GTN are also in Payrun.
6. **GTN elements missing in Payrun** – Checks if mapped GTN pay elements exist in Payrun.
7. **Payrun elements missing in GTN** – Checks if mapped Payrun pay elements exist in GTN.
8. **Numeric values** – Checks that GTN pay element columns have numeric values.

## Test Data Folders

- Each test has a **fail-case folder**: contains files modified to fail the specific test.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
