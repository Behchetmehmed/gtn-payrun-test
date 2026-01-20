import pandas as pd
import unittest
import json
import main

class TestPayrunMapping(unittest.TestCase):

    def setUp(self):
        #file directories
        self.gtn_file = "Files/GTN.xlsx"
        self.payrun_file = "Files/Payrun.xlsx"
        self.mapping_file = "Files/mapping.json"

        #reading files
        self.gtn_df = pd.read_excel(self.gtn_file)
        self.pay_df = pd.read_excel(self.payrun_file)

        with open(self.mapping_file, 'r') as f:
            self.mapping_df = json.load(f)["mappings"]


    def test_file_type(self):

        self.assertTrue(self.gtn_file.lower().endswith(".xlsx"), "File is not type .xlsx!")
        self.assertTrue(self.payrun_file.lower().endswith(".xlsx"), "File is not type .xlsx!")


    def test_line_breaks(self):

        self.assertFalse(self.gtn_df.isnull().all(axis=1).any(), "File contains empty rows")

    def test_header(self):

        self.assertEqual(len(self.gtn_df.columns.names), 1, "The Gtn header structure has changed!")

    def test_missing_employees_in_payrun(self):
        pays = set(self.pay_df['Employee ID'])
        cust = set(self.gtn_df['employee_id'])
        missing = pays - cust
        self.assertFalse(missing, f"Employees are missing in gtn file: {missing}")

    def test_missing_employees_in_gtn(self):
        pays = set(self.pay_df['Employee ID'])
        cust = set(self.gtn_df['employee_id'])
        missing = cust - pays
        self.assertFalse(missing, f"Employees are missing in gtn file: {missing}")

    def test_gtn_elements_missing_in_payrun(self):
        gtn_elements = self.gtn_df.columns[4:]
        payrun_elements = self.pay_df.columns[25:]

        missing = []

        for e in gtn_elements:

            if e in self.mapping_df and self.mapping_df[e]["map"]:
                payrun_col = self.mapping_df[e]["vendor"]
                if payrun_col not in payrun_elements:
                    missing.append(payrun_col)

        self.assertFalse(missing, f"GTN missing elements in  Payrun: {missing}")

    def test_pay_elements_missing_in_gtn(self):
        gtn_elements = self.gtn_df.columns[4:]
        payrun_elements = self.pay_df.columns[25:]

        missing = []

        for e in gtn_elements:

            if e in self.mapping_df and self.mapping_df[e]["map"]:
                df_col = self.mapping_df[e]["vendor"]
                if df_col not in payrun_elements:
                    missing.append(df_col)

        self.assertFalse(missing, f"Payrun missing elements in  GTN: {missing}")




    def test_gtn_numeric_columns(self):
        columns = self.gtn_df.columns[4:]
        non_numeric = []
        for col in columns:
            for value in self.gtn_df[col]:
                if not isinstance(value, (int, float)):
                    non_numeric.append(col)
                    break
        self.assertFalse(non_numeric, f"These columns are non-numeric: {', '.join(non_numeric)}")



if main == "__main__":
    unittest.main()