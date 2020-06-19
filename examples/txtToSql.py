import os
import sys
sys.path.append("..")
from src.sqlconverter import Table

PATH = sys.argv[1]
TABLE_NAME = PATH[:PATH.find('.')]
SLQ_PATH = sys.argv[2]

tb = Table()
tb.get_data_from_txt(PATH, separator=";", quiet=False)
tb.insert_sql(SLQ_PATH, types=sys.argv[3:], tablename=TABLE_NAME, create_new_table=True)
tb.summary()