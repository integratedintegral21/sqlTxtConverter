import os
import sys
sys.path.append("..")
from src.sqlconverter import Table



PATH = sys.argv[1]
TABLE_NAME = PATH[:PATH.find('.')]
SLQ_PATH = sys.argv[2]

tb = Table()
tb.get_data_from_txt(PATH, ';', quiet=True)
tb.create_and_insert_sql(SLQ_PATH, types=sys.argv[3:], tablename=TABLE_NAME)