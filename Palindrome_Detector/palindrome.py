'''
This prgram checks if the user input is a palindrome.
Palindrome
03 June 2021
Bruce Mvubele
'''

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
        # Everytime function is called it slices first element of string until
        # base case is met (len(string) = 1) it then unpacks. taking the first 
        # element from the previous call and adds it to reverse variable
        reverse = IsPalindrome(string[1:]) + string[0]
        #print(f'string ={string}, reverse ={reverse}')
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