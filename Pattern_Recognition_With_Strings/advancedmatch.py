# This program tests if a user input string containg '?' as placeholders for 
# current characters and '*' as a place holder for current and following characters
# 05 June 2021
# Bruce Mvubele

def match(pattern, word):
    ''' Checks if 'word' is a match to 'pattern'
    
    Parameters
    ----------
    pattern : str
        User input containing '?' and '*' as wildcards.
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
    
    if len(pattern) > 1 and pattern[0] == '*' and len(word) == 0:
        return False
     # if pattern contains '?' and current charcters of word match current character pattern iterate
    if (len(pattern) > 1 and pattern[0] == '?') or  (len(pattern) != 0 and len(word) !=0 and pattern[0] == word[0]):
        return match(pattern[1:],word[1:])
    # if pattern is not empty and pattern has '*' slice '*' and iterate
    if len(pattern) != 0 and pattern[0] == '*':
        return match(pattern[1:], word) or match(pattern, word[1:])
    
    return False

def main():
    pattern = input('Enter a pattern (or press \'q\' to quit):\n')
    
    while pattern != 'q':
        word = input('Enter a word\n')
        if match(pattern,word):
            print("It's a match.")
        else:
            print('They don\'t match')
        pattern = input('Enter a pattern (or press \'q\' to quit):\n')

        

        
if __name__ == '__main__':
    main()