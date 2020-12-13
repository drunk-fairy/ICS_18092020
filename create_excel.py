import xlsxwriter

from data import data_

def generateExcel():

    workbook = xlsxwriter.Workbook('e:/University/ВКН індивідуальний_проект/table.xlsx')

    sheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    for i in range (0, len(letters)):
        sheet.set_column(f'{letters[i]}:{letters[i]}', 23)

    # the following piece of code does funny shit so I didn't want to delete it

    #for i, k in zip(range (1, (len(data_)+1)), range (0, 6)):
        #sheet.write(f'{letters[k]}{i}', f'{data_[i-1][k]}', bold)

    for i in range (0, (len(data_)+1)):
        for k in range (0, len(letters)):
            sheet.write(f'{letters[k]}{i}', f'{data_[i-1][k]}', bold)

    workbook.close()