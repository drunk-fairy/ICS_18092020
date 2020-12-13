import json
import sys

from data import data_

def convertToJSON():
    with open('E:/University/ВКН індивідуальний_проект/data_file.json', 'w') as write_file:
        json.dump(data_, write_file)
