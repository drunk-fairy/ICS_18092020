from prettytable import PrettyTable

from data import data_

#print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
#for item in data_:
    #print('|', item[0], ' '*(12-len(item[0])), '|',\
            #item[1], ' '*(22-len(item[1])), '|',\
            #item[2], ' '*(18-len(str(item[2]))), '|',\
            #item[3], ' '*(15-len(str(item[3]))), '|',\
            #item[4], ' '*(13-len(str(item[4]))), '|',\
            #item[5], ' '*(18-len(str(item[5]))), '|',\
            #item[6], ' '*(22-len(str(item[6]))), '|',\
                   #)
#print('-----------------------------------------------------------------------------------------------------------------------------------------------------')

                    
x = PrettyTable()

x.field_names = data_[0]

for i in range (1, len(data_)):

    x.add_rows(
        [
            data_[i]
        ]
    )

def showTable():
    print('\nАНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ')
    print(x)