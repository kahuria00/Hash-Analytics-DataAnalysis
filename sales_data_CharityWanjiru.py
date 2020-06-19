import pandas as pd 

sheets=['Sheet1','Sheet2','Sheet3','Sheet4','Sheet5','Sheet6','Sheet7','Sheet8','Sheet9','Sheet10']

saleData=pd.read_excel("C:/Users/Admin/Documents/HashAnalyticsProjects/sales_data.xlsx",sheet_name=sheets)



for sheet_name, data in saleData.items():
    sheets = sheet_name
    data.to_csv(f'{sheet_name}.csv', header=False)








	