import pandas as pd
#pyinstaller --onefile Project_3_Automate_excel_report_py_to_exe.py
#6 - py to exe

import os
import sys

application_path=os.path.dirname(sys.executable)

#1- Create a pivot table
input_path=os.path.join(application_path, 'supermarket_sales.xlsx')
df=pd.read_excel(input_path)

df=df[['Gender','Product line','Total']]
pivot_table = df.pivot_table(index='Gender', columns='Product line', \
                             values='Total', aggfunc='sum').round(0)


output_path=os.path.join(application_path,'Output_Project_3_py_to_exe.xlsx')
pivot_table.to_excel(output_path, 'Report', startrow=4)

