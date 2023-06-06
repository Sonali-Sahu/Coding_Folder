# Given a string, count total number of consonants in it.
# A consonant is an English alphabet character that is not vowel (a, e, i, o and u). 
# Examples of constants are b, c, d, f, and g.


def isConsonant(ch):
    ch = ch.upper()
  
    return not (ch == 'A' or ch == 'E' or 
                ch == 'I' or ch == 'O' or 
                ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
  
def totalConsonants(string, n):
      
    if n == 1:
        return isConsonant(string[0])
  
    return totalConsonants(string, n - 1) + isConsonant(string[n-1])
 
string = "abc de"
print(totalConsonants(string, len(string)))
  
