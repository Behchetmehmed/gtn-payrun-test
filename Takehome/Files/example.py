import pandas as pd

df_customer = pd.read_excel("GTN.xlsx")
df_payslip = pd.read_excel("Payrun.xlsx")


print(df_payslip.columns)