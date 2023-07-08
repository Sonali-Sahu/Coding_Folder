# Q1. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
def decimalToRoman(num):
    roman_symbols = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    roman_numeral = ""
    for value, symbol in roman_symbols.items():
        while num >= value:
            roman_numeral += symbol
            num -= value

    return roman_numeral


# Example usage
decimal_number = 356
roman_number = decimalToRoman(decimal_number)
print(roman_number)  # Output: CCCLVI




#2. **Longest Substring Without Repeating Characters**

# Given a string `s`, find the length of the **longest substring** without repeating characters.


def lengthOfLongestSubstring(s):
    # Initialize variables
    longest_length = 0
    start = 0
    char_map = {}

    # Iterate over the string
    for end in range(len(s)):
        # Check if the current character is already seen in the substring
        if s[end] in char_map:
            # Update the start index to the next position after the last occurrence of the current character
            start = max(start, char_map[s[end]] + 1)

        # Update the length of the longest substring
        longest_length = max(longest_length, end - start + 1)

        # Update the last seen position of the current character
        char_map[s[end]] = end

    return longest_length


# Example usage
string = "abcabcbb"
length = lengthOfLongestSubstring(string)
print(length)  # Output: 3

# Q3. Given an array `nums` of size `n`, return *the majority element*.

# The majority element is the element that appears more than `⌊n / 2⌋` times.
# You may assume that the majority element always exists in the array.


def majorityElement(nums):
    count = 0
    candidate = None

    # Find a candidate for the majority element using Boyer-Moore Voting Algorithm
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# Example usage
nums = [2, 2, 1, 1, 1, 2, 2]
majority = majorityElement(nums)
print(majority)  # Output: 2



# Q4. Given an array of strings `strs`, group **the anagrams** together. 
# You can return the answer in **any order**.

# An **Anagram** is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict

def groupAnagrams(strs):
    # Create a dictionary to store groups of anagrams
    anagram_groups = defaultdict(list)

    # Iterate over each string in the input array
    for s in strs:
        # Sort the string to obtain a unique key for anagrams
        sorted_s = "".join(sorted(s))
        # Append the current string to the corresponding anagram group
        anagram_groups[sorted_s].append(s)

    # Convert the dictionary values (anagram groups) to a list
    grouped_anagrams = list(anagram_groups.values())

    return grouped_anagrams


# Example usage
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_groups = groupAnagrams(strings)
print(anagram_groups)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# Q5. An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

# Given an integer `n`, return *the* `nth` ***ugly number***.


def nthUglyNumber(n):
    ugly_numbers = [1]  # Initialize the list with the first ugly number
    i2, i3, i5 = 0, 0, 0  # Pointers for multiplying by 2, 3, and 5

    while len(ugly_numbers) < n:
        # Calculate the next ugly number as the minimum among the multiples of 2, 3, and 5
        next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)

        ugly_numbers.append(next_ugly)  # Append the next ugly number to the list

        # Update the pointers based on which number was used to calculate the next ugly number
        if next_ugly == ugly_numbers[i2] * 2:
            i2 += 1
        if next_ugly == ugly_numbers[i3] * 3:
            i3 += 1
        if next_ugly == ugly_numbers[i5] * 5:
            i5 += 1

    return ugly_numbers[-1]


# Example usage
n = 10
ugly_number = nthUglyNumber(n)
print(ugly_number)  # Output: 12


# Q6. Given an array of strings `words` and an integer `k`, return *the* `k` *most frequent strings*.

# Return the answer **sorted** by **the frequency** from highest to lowest.
# Sort the words with the same frequency by their **lexicographical order**.


from collections import Counter

def topKFrequent(words, k):
    # Count the frequency of each word in the input array
    word_counts = Counter(words)

    # Sort the words based on frequency and lexicographical order
    sorted_words = sorted(word_counts.keys(), key=lambda word: (-word_counts[word], word))

    # Return the top k frequent words
    return sorted_words[:k]


# Example usage
word_array = ["apple", "banana", "apple", "orange", "banana", "apple", "pear"]
k = 2
top_k_frequent = topKFrequent(word_array, k)
print(top_k_frequent)
# Output: ['apple', 'banana']



# Q7. You are given an array of integers `nums`, there is a sliding window of size `k`
# which is moving from the very left of the array to the very right. 
# You can only see the `k` numbers in the window. Each time the sliding window
# moves right by one position.

# Return *the max sliding window*.

from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    window = deque()

    # Process the first k elements separately to initialize the window
    for i in range(k):
        # Remove any elements from the window that are smaller than the current element
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # Add the current element's index to the window
        window.append(i)

    # Process the remaining elements using the sliding window approach
    for i in range(k, len(nums)):
        # The front of the window represents the maximum element for the current window
        result.append(nums[window[0]])

        # Remove elements from the window that are outside the current window range
        while window and window[0] <= i - k:
            window.popleft()

        # Remove any elements from the window that are smaller than the current element
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # Add the current element's index to the window
        window.append(i)

    # Add the maximum element for the last window
    result.append(nums[window[0]])

    return result


# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_window = maxSlidingWindow(nums, k)
print(max_window)
# Output: [3, 3, 5, 5, 6, 7]


# Q8. Given a sorted integer array arr, two integers k and x, return the k 
# closest integers to x in the array. The result should also be sorted in ascending order.

def findClosestElements(arr, k, x):
    # Binary search to find the closest element to x
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    # Return the k closest elements from the found starting index
    return arr[left:left + k]


# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
x = 4
closest_elements = findClosestElements(arr, k, x)
print(closest_elements)
# Output: [3, 4, 5]







