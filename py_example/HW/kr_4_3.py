'''
Вызов функции: find_most_frequent('Hello, hello, my dear!')
Возвращает: ['hello']

Вызов функции: find_most_frequent('to understand recursion you need first to understand recursion...')
Возвращает: ['recursion', 'to', 'understand']
'''


def find_most_frequent(text):
    if :
        return text
    text = text.lower().split()
    temp_d = {}
    clean_word = []
    res = []
    for item in text:
        item = item.rstrip(',.:;!?')
        clean_word.append(item)
    for item in clean_word:
        temp_d[item]=clean_word.count(item)

    maximum=temp_d[max(temp_d ,key= temp_d.get)]
    for index, item in temp_d.items():
        if item == maximum:
            res.append(index)
    res.sort()
    return res





print(find_most_frequent('to understand, recursion you need first to understand recursion...'))
print(find_most_frequent('Hello, hello, my dear!'))
print(find_most_frequent('Python is simple to use.'))
print(find_most_frequent(''))