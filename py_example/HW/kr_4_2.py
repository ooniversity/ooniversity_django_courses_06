# def trim_trim(text):
#    while text[-1] != ' ':
#        text = text[0:-1]
#
#    return text.strip(' .,:!?;')
#
#
# def trimmed_text(text,limit):
#    res =''
#    len_var = len(text)
#    text_tmp = text[0:limit-1]
#    if text_tmp.rfind(' ') == -1:
#        res = text[0:limit - 3] + '...'
#    else:
#        if limit >= len(text):
#            res = text
#        elif  text[limit-1] != ' ':
#            text_tmp = trim_trim(text_tmp)
#            res = text_tmp+'...'
#        else:
#            res = text_tmp+'...'
#    return res
def  trimmed_text(text,limit):
    pattern= '...'
    var_text_len = len(text)
    if limit < var_text_len:
        index = text.rfind(' ',0,(limit-2))
        if index == -1:
            index = limit-len(pattern)
        text= text[:index].rstrip(',.:;!?')+pattern
    return text

    print(trimmed_text("Proin eget tortor risus.", 23))
print(trimmed_text("Proin eget tortor risus.", 6))
print(trimmed_text("Proin eget tortor risus.", 24))
print(trimmed_text( 'Python is simple to use, but it is a real programming language.', 64))
print(trimmed_text( 'Python is simple to use, but it is a real programming language.', 62))
print(trimmed_text( 'Python is simple to use, but it is a real programming language.', 33))