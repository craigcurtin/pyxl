# option 2: concatenate them first using pd.concat() and then apply the function only once.
excel_file_1 = pd.read_excel('Data/sales_01.xlsx')
excel_file_2 = pd.read_excel('Data/sales_02.xlsx')
excel_file_3 = pd.read_excel('Data/sales_03.xlsx')

new_file = pd.concat([excel_file_1,
                      excel_file_2,
                      excel_file_3], ignore_index=True)
new_file.to_excel('sales_2021.xlsx')
automate_excel('sales_2021.xlsx')