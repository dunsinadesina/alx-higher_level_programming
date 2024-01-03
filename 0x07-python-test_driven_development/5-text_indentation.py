#!/usr/bin/python3
"""
module indentation
 prints a text with 2 new lines after each of these characters: ., ? and :
 """
def text_indentation(text):
    """
    prints texts with extra two lines after each of these characters(., ? and :)
    """
    
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
         text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
