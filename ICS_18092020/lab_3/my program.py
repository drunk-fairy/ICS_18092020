word = list('электрификация')
import random
random.shuffle(word)
print ('Введите правильно слово:')
for i in word:
    print(i, end=' ')
word2 = input()
if word2 == 'электрификация':
    print('Отлично!')
else:
    print('Ошибка')



        
