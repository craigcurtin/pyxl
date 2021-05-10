from xl_auto import xl_auto
import logging
from util_logger import setup_logger

if __name__ == '__main__':
    setup_logger('xl_batch', 'c:/Temp/', logging.DEBUG)
    try:
        xl_auto('Data/sales_01.xlsx')
        xl_auto('Data/sales_02.xlsx')
        xl_auto('Data/sales_03.xlsx')
    except Exception as ex:
        logging.exception('Exception raised ..... uh, oh!')
