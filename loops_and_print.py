def enumerate_list(list):
    result = []
    index = 0
    for string in list:
        if string:
            result.append (f"{index}. {string}")
            index +=1
    return result




def enumerate_backwards(list):
    result = []
    index = 0
    for string in list:
        if string:
            result.append (f"{index}. {string[ : :-1]}")
            index +=1
    return result










