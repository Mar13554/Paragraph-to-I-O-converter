#Takes in paragraph and turns it to I/O (Words pair)
import re

pattern = r"[\n\t]"
def convert_w(paragraph, list_number):
    #Remove \n and \t
    paragraph = re.sub(pattern, " ", paragraph)
    #Convert from paragraph to list of words
    length_paragraph = len(paragraph)
    word_list = []; word = ""
    #Loop to go through
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
    MainDict = {str(list_number):SubDicts}
    return MainDict

def convert_s(paragraph, list_number):
    # Remove \n and \t
    paragraph = re.sub(pattern, " ", paragraph)
    paragraph.strip()
    #Define
    punctuation_symbols = [".", "?", "!"] #For sentences
    sentence_list = []; sentence = ""; is_of_symbol = False; delay_sentence_by = 0

    #Create sentences list
    #For each letter (integer in the string)
    for letter_num in range(0, len(paragraph)):
        #Search if the letter is of that symbol
        for j in punctuation_symbols:
            if paragraph[letter_num] == j:
                is_of_symbol = True
                break
        #Check and execute
        if is_of_symbol:
            #Check case of ." Quotes
            try:
                if paragraph[letter_num+1] == "'" or paragraph[letter_num+1] == '"':
                    sentence += paragraph[letter_num]
                    delay_sentence_by = 1
            except IndexError:
                pass
            #Create new sentence if allowed and not empty
            if sentence != "" and delay_sentence_by == 0:
                sentence += paragraph[letter_num]
                sentence_list.append(sentence)
                sentence = ""
        else:
            #Check if it was delayed or not to create
            if delay_sentence_by == 1:
                delay_sentence_by -= 1
                sentence += paragraph[letter_num]
                sentence_list.append(sentence)
                sentence = ""
            else:
                #Add the letter to the sentence
                sentence += paragraph[letter_num]
        is_of_symbol = False
    #Convert sentence list to pairs in dict
    amount_of_sentences = len(sentence_list)
    SubDicts = {}
    for i in range(0, amount_of_sentences-1):
        SubDicts.update({str(i+1):{"input":(sentence_list[i].strip()), "output":(sentence_list[i+1].strip())}})
    MainDict = {str(list_number):SubDicts}
    return MainDict
