def checker(tmp,index,len):
    if index == len :
        tmp = tmp+'_'
    elif index == 0:
        tmp = tmp + '_ '
    elif tmp[-1] != ' ':
        tmp = tmp + ' _'
    else:
        tmp = tmp + '_ '
    return tmp

def hangman(word, letters):
    tmp = ''
    for index ,item in enumerate(word):
        if len(letters) == 0:
            letters.append('0')
        l = len(word)
        if item not in letters:
             tmp = checker(tmp,index,l)
        else:
            if len(tmp)!=0 and tmp[-1] == '_':
                tmp = tmp + ' '+item
            else:
                tmp = tmp + item

    print(tmp.strip())
    return tmp

hangman('hangman', ['q', 'w', 'e', 's', 'f', 'z', 'v'])
hangman('hangman', ['p', 'i', 'a'])
hangman('hangman', ['0'])
hangman('hangman', ['h', 'j', 'a', 'o', 'n'])
hangman('hangman',  ['n', 'g', 'u', 't'])
hangman('hangman', ['h', 'a', 'n', 'g', 'm'])