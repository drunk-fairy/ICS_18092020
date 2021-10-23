from tkinter import *

from create_plots import showPlot
from create_table import showTable
from create_table import x
from convert_to_json import convertToJSON
from create_doc import saveDOCX
from create_excel import generateExcel

root = Tk()
root.title('РУХ ОСНОВНИХ ЗАСОБІВ')
root.geometry('300x300')
root.resizable(False, False)
root.configure(bg = 'gray22')

def openPlot():
    showPlot()

def openTable():
    showTable()
    root_2 = Tk()
    root_2.geometry('1400x300')
    root_2.title('АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ')
    lbl = Label(root_2)
    lbl.configure(font = (7), text = x)
    lbl.place(x = 0, y = 0)
    root_2.mainloop()

def createJSON():
    convertToJSON()
    root_3 = Tk()
    root_3.geometry('200x70')
    root_3.resizable(False, False)
    root_3.title('повідомлення')
    lbl = Label(root_3)
    lbl.configure(font = (5), text = 'Файл у форматі \nJSON сформовано')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()

def createDOCX():
    saveDOCX()
    root_4 = Tk()
    root_4.geometry('200x70')
    root_4.resizable(False, False)
    root_4.title('повідомлення')
    lbl = Label(root_4)
    lbl.configure(font = (5), text = 'Файл у форматі \nDOCX сформовано')
    lbl.place(x = 4, y = 2)
    root_4.mainloop()

def createExcel():
    generateExcel()
    root_4 = Tk()
    root_4.geometry('200x70')
    root_4.resizable(False, False)
    root_4.title('повідомлення')
    lbl = Label(root_4)
    lbl.configure(font = (5), text = 'Таблицю \nExcel сформовано')
    lbl.place(x = 4, y = 2)
    root_4.mainloop()

btn1 = Button(root)
btn1.configure(bg = 'gray', fg = 'white', text = 'відкрити графік', command = openPlot)
btn1.place(x = 90, y = 20, width = 120, height = 30)

btn2 = Button(root)
btn2.configure(bg = 'gray', fg = 'white', text = 'відкрити таблицю', command = openTable)
btn2.place(x = 90, y = 70, width = 120, height = 30)

btn3 = Button(root)
btn3.configure(bg = 'gray', fg = 'white', text = 'створити файл json', command = createJSON)
btn3.place(x = 90, y = 120, width = 120, height = 30)

btn4 = Button(root)
btn4.configure(bg = 'gray', fg = 'white', text = 'створити файл docx', command = createDOCX)
btn4.place(x = 90, y = 170, width = 120, height = 30)

btn5 = Button(root)
btn5.configure(bg = 'gray', fg = 'white', text = 'створити файл xlsx', command = createExcel)
btn5.place(x = 90, y = 220, width = 120, height = 30)



root.mainloop()