
def print_upper_words(words, must_start_with={'h', 'y'}):
    """Function accepts a list of words.
    Function prints each word on a new line, but in all uppercase."""
    # check everything in must_start_with is already .lower()
    for word in words:
        if not(word[0].lower() in must_start_with):
            continue
        cap_word = ''
        for char in word:
            cap_word += char.upper()
        print(cap_word)

print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'])
