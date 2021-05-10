from xl_auto import xl_auto

if __name__ == '__main__':
    xl_file_1 = pd.read_excel('Data/sales_01.xlsx')
    xl_file_2 = pd.read_excel('Data/sales_02.xlsx')
    xl_file_3 = pd.read_excel('Data/sales_03.xlsx')

    new_file = pd.concat([xl_file_1,
                          xl_file_2,
                          xl_file_3], ignore_index=True)
    new_file.to_excel('sales_2021.xlsx')
    xl_auto('sales_2021.xlsx')
