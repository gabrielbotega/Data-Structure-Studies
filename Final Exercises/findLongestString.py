"""
List: Find Longest String ( ** Interview Question)
Write a Python function called find_longest_string that takes a list of strings as an input and returns the 
longest string in the list. The function should iterate through each string in the list, check its length, and keep 
track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.



Example:

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'
"""

# easiest way to implement. However, this is not a time complexity optimized method. O(n)
def find_longest_string(arr):
    if len(arr) ==0:
        return ""
    bigger  = 0
    for index, string in enumerate(arr):
        if len(string) > len(arr[bigger]):
            bigger  = index

    return arr[bigger]

        

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""