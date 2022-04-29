# This program checks for palindrome primes within an interval specified by the user.
# 03 Jube 2021
# Bruce Mvubele

LOWER = input('Enter lower limit:\n')
UPPER = input('Enter upper limit:\n')

INTERVAL = list(range(int(LOWER),int(UPPER) + 1))

prime_list = []
def IsPrime(interval):
    '''Extracts primes from interval'''
    global prime_list
    for i in interval:
        if i % 2 != 0:
            prime_list.append(i)
             
IsPrime(INTERVAL)

def reverser(string):
    ''' Reverses string

    Parameters:
    ----------
    string : str
        
    Returns:
    -------
    str
    Reversed version of input
    '''
    string = str(string)
    if len(string) != 1:
        # Everytime function is called it slices first element of string until
        # base case is met (len(string) = 1) it then unpacks. taking the first 
        # element from the previous call and adds it to reverse variable
        reverse = reverser(string[1:]) + string[0]
        #print(f'string ={string}, reverse ={reverse}')
        return reverse
    else:
        return string

reversed_prime = []
for i in prime_list:
    # Extract palindrome primes
    if str(i) == str(int(reverser(i))):
        reversed_prime.append(i)

print(f'The list of palindrome primes in the interval [{LOWER},{UPPER}] is {reversed_prime}')
