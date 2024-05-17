def enumerate_list(list):
    result = []
    index = 0
    for string in list:
        if string:
            result.append (f"{index}. {string}")
            index +=1
    return result


print(enumerate_list(["Red", "Green", "", "White", "Black"]))









