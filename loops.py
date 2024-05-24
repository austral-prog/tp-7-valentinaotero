def index_of_by_index(word, list, index):
    counting = 0
    new_list = list[index:]
    while counting < len(new_list):
        new_word = new_list[counting]
        if new_word == word:
            return counting + index
        counting += 1
    return -1


def index_of_empty(list):
    counting = 0
    while counting < len(list):
        new_element = list[counting]
        if new_element == "":
            return counting
        counting += 1
    return -1


def index_of(word, list):
    counting = 0
    while counting < len(list):
        if word == list[counting]:
            return counting
        counting += 1
    return -1


def put(word, list):
    counting = 0
    for element in list:
        if element == "":
            list[counting] = word
            return counting
        counting += 1
    return -1


def remove(word, list):
    deleted_words = 0
    for index in range(len(list)):
        if list [index] == word:
            list [index] = ""
            deleted_words += 1
    return deleted_words



















