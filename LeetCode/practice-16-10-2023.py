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


# HashMap way 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        countS,countT = {},{}
        for ch in s:
            if ch in countS:
                countS[ch] += 1
            else:
                countS[ch] = 1

        for ch in t:
            if ch in countT:
                countT[ch] += 1
            else:
                countT[ch] = 1
        value_flag = 1

        for ch_key,ch_value in countS.items():
            if ch_key not in countT:
                value_flag = 0
            if  ch_key in countT and countT[ch_key] != ch_value:
                value_flag = 0

        if value_flag:
            return True
        else:
            return False


# sorted way



        
