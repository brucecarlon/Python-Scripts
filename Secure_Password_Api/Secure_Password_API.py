# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:52:30 2021
This program is a password checker, it takess an input from user runs it through a hash function extracts the first five characters
and compares them to passwordson pwnedpasswords response
@author: Bruce mvubele
"""
# sername = input('Enter username ')
# password = input('Enter password ')
# length = len(password)
# hiden_pasword = length*"*"
# print(f'Hi {username}, your password', hiden_pasword,' is', length,' characters long')




import requests
import hashlib
import sys

user_password = input("Enter password:\n")

def request_api_data(query_char):  # query_char is the five digits from the hash code
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
       
    return res


# returns all the entries that have a password that matches the query character.
# the seond number after the colon shows you how many times it been found


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count) 
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #check password if it exists in api response
    
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  #encrypted password
    first5_char, tail  = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
   
    
    return get_password_leaks_count(response, tail)

def main(args): # password we want to check

    count = pwned_api_check(args)
    if count:
        print(f'{args} was found {count} times.. you should change password')
    else:
        print(f'{args} was NOT found. Carry on!')
    return 'done!'
    
if __name__ =='__main__':
    main(user_password) 