import os
import sys
sys.path.append("..")
from src.sqlconverter import Table

PATH = "wypozyczenia.txt"
TABLE_NAME = PATH[:PATH.find('.')]
SLQ_PATH = TABLE_NAME + '.sql'
    

tb = Table()
tb.get_data_from_txt(PATH, ';', quiet=True)
tb.insert_sql(SLQ_PATH, types=["int", "DATE", "DATE", "DATE"], tablename=TABLE_NAME)