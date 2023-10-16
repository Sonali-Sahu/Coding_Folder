# Q1. Valid anagram
string1 = 'anagram'
string2 = 'nagaran'

string2_list = list(string2)
# print(string2_list)

if len(string1) != len(string2):
    print("False, Length is not same")
else:
    for ch in string1:
        if ch in string2_list:
            string2_list.remove(ch)
        
    
if len(string2_list) == 0:
    print('True, Strings are anagram')
else:
    print('False, Strings are not anagram')
    
