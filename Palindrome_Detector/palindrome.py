USER_INPUT = input('Enter a string:\n')

def IsPalindrome(string):
    ''' Checks if a string is a palindrome

    Parameters:
    ----------
    string : str
        
    Returns:
    -------
    Reversed version of input :  str 
    '''

    if len(string) != 1:
        reverse = IsPalindrome(string[1:]) + string[0]
        return reverse
    else:
        return string

def main():
    if USER_INPUT == '':
        print('Palindrome!')  
    elif  USER_INPUT == IsPalindrome(USER_INPUT):
        print('Palindrome!')
    else:
        print('Not a palindrome!')
        
if __name__ == '__main__':
    main()




    # Let the isPalindrome function be denoted by f(string)
    # string = 'cake'
    # reverse = f(ake) + c
    #         = f(f(ke) + a) +c
    #         = f(f(f(e)+ k ) + a) + c
    #         = e+k+a+c = ekac
    #