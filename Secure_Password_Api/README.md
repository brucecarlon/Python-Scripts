# Secure-Password-API
This program is a secure password checker, it takes a password input from a user, runs it through the SHA1 hash function and extracts the first five characters of the hash key.
We then compare them to passwords on pwnedpasswords and returns a list of such passwords that match the five first characters. We then check for a password with the rest of characters of its hash key that matches to the rest of the charcters of the user password hash key. The security is ensured by never passing the user password as a a string but rather passes only a portion of the hashed user password that matches to a variety of hash keys.\
Program returns the number of times your password has been retrieved in database breach.
