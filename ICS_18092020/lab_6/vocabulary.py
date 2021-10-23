class Vocabulary():
    def __init__(self, english_value, russian_value):
        self.english_value = english_value
        self.russian_values = [russian_value]

words_and_transl = {
                    'nails': ['нігті', 'цвяхи'],
                    'mine': ['мій', 'шахта', 'міна'],
                    'draft': ['протяг', 'чернетка', 'призов'],
                    'current': ['теперішній', 'течія']
                    }
w1 = 'mine'
w2 = 'nails'
w3 = 'draft'
w4 = 'current'

print(f'{w1} {words_and_transl[w1]}')
print(f'{w2} {words_and_transl[w2]}')
print(f'{w3} {words_and_transl[w3]}')
print(f'{w4} {words_and_transl[w4]}')