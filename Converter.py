#Takes in paragraph and turns it to I/O (Words pair)
def convert_w(paragraph):
    #Convert from paragraph to list of words
    length_paragraph = len(paragraph)
    word_list = []; word = ""
    for i in range(0, length_paragraph):
        if paragraph[i] != " ":
            word += paragraph[i]
        else:
            if word != "":
                word_list.append(word)
                word = ""
    #Catch final word
    if word != "":
        word_list.append(word)

    #Convert from list of words to dict
    length_list_words = len(word_list)
    SubDicts = {}
    # One to one pair
    for i in range(0, length_list_words-1):
        SubDicts.update({str(i+1):{"input":word_list[i], "output":word_list[i+1]}})
    MainDict = {"1":SubDicts}
    return MainDict
