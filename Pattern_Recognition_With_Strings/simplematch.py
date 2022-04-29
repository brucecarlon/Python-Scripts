# This program tests if a user input as a string matches
# to second string string containing '?' as wildcards.
# 04 June 2021
# Bruce Mvubele

def match(pattern, word):
    ''' Checks if 'word' is a match to 'pattern'
    
    Parameters
    ----------
    pattern : str
        User input containing '?' as wildcards.
    word : str
        User inputs a word to be compared to pattern.

    Returns
    -------
    bool
        True if word matches pattern .

    '''
    # Base case: stop if word and pattern are empty strings
    if len(pattern) == 0 and len(word) == 0:
        return True
     
    # If word is an empty string they don't match
    if len(pattern) > 1 and pattern[0] == '?' and len(word) == 0:
        return False
    
    # if pattern contains '?' and charcters of word pattern match they words match
    if (len(pattern) >= 1 and pattern[0] == '?') or  (len(pattern) != 0 and len(word) !=0 and pattern[0] == word[0]):
        return match(pattern[1:],word[1:])
    return False

def main():
    pattern = input('Enter a pattern (or press \'q\' to quit):\n')
    
    while pattern != 'q':
        word = input('Enter a word\n')
        if match(pattern,word) == True:
            print("It's a match.")
        else:
            print('They don\'t match')
        pattern = input('Enter a pattern (or press \'q\' to quit):\n')

        

        
if __name__ == '__main__':
    main()