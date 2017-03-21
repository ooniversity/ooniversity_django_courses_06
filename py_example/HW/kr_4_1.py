def double_tuple(value):
    index = 0
    new_tuple = []
    tmp_tuple = ()
    for item in range(0, len(value), 2):
        index = item + 1
        l = len(value) - 1
        if item == l:
            tmp_tuple = (value[item],)
        else:
            y = value[item]
            z = value[index]
            tmp_tuple = (y, z)
        new_tuple.append(tmp_tuple)
    return tuple(new_tuple)


print(double_tuple((1, 2, 3, 4)))