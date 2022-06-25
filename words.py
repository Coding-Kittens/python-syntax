def  print_upper_words(words, must_start_with = None):
    """ Turns words into all UPPER CASE and prints them.

If there are any letters in the list must_start_with
then it checks if the word starts with any of thoughs letters

    """
    for word in words:
        if must_start_with == None:
            print(word.upper())
        else:
            for char in must_start_with:
                if word[0] == char.lower() or word[0] == char.upper():
                    print(word.upper())








print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with=["h", "y"])
