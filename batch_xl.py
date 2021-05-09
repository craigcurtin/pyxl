from xl_auto import automate_excel

if __name__ == '__main__':
    try:
        automate_excel('Data/sales_01.xlsx')
        automate_excel('Data/sales_02.xlsx')
        automate_excel('Data/sales_03.xlsx')
    except