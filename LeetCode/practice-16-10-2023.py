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
#  used built-in sorted method




# occurence counter of string using dict
sample_string = "this is my home"
counterS = {}
# using single statement
for i in range(len(sample_string)):
    if sample_string[i] != " ":
        counterS[sample_string[i]] = 1 + counterS.get(sample_string[i],0)
    
print(counterS)




# merge two arrays
arr1 = [0,1,2,3,5]
arr2 = [2,3,4,]
len_a1 = len(arr1)
len_a2 = len(arr2)
n = len_a1 + len_a2
result_arr = [0]*n
i = 0
j = 0
k = 0
while  i < len_a1 and j <  len_a2 :
    if arr1[i] < arr2[j] :
        result_arr[k] = arr1[i]
        i +=1
        k += 1
    else:
        result_arr[k] = arr2[j]
        j += 1
        k += 1
    
    
while  i < len_a1:
    result_arr[k] = arr1[i]
    i += 1
    k += 1

while  j < len_a2:
    result_arr[k] = arr2[j]
    j += 1
    k += 1    
    
    
print(result_arr)
    





        
