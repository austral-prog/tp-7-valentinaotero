def enumerate_list(list):
    new_list = []
    index = 0
    for string in list:
        if string != "":
            new_element = f"{index}. {string}"
            new_list.append(new_element)
            index +=1
    return new_list


def enumerate_backwards(list):
    result = []
    index = 0
    for string in list:
        if string:
            new_element = f"{index}. {string[ : :-1]}"
            result.append (new_element)
            index +=1
    return result





