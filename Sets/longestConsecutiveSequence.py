"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e.,
sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
"""
# def longest_consecutive_sequence(nums):
#     indexEValor = []
#     dic ={}
#     dicRetrieve ={}

#     nums = set(nums)
#     nums = list(nums)

#     for i, value in enumerate(nums):
#         for k, val in enumerate(nums[i+1:],i+1):
#             dif = value - val
#             if -len(nums)+i <= dif <= len(nums)-i :
#                 indexEValor.append([i,k, dif])
#                 # indexEValor.append(nums[i])
#                 # indexEValor.append(nums[k])
#     for i in indexEValor:
#         if i[0] not in dicRetrieve:
#             dicRetrieve[i[0]] = []
#         dicRetrieve[i[0]].append(nums[i[1]])

#     for i in indexEValor:
#         if i[0] not in dic:
#             dic[i[0]] = []
#         dic[i[0]].append(i[2])

#     for key, value in dic.items():
#         temporario = []
#         tamanho = len(value)
#         for i in value:
#             if i < 0:
#                 i = - i
#             temporario.append(i)
#         temporario.append(key)
#         if max(temporario[:-1]) == tamanho and min(temporario[:-1]) == 1:
#             break
    
#     listToReturn = [* dicRetrieve [temporario[tamanho]],  nums[temporario[tamanho]]]
#     return len(listToReturn)
#     # print((indexEValor))
#     # print((dicRetrieve))
#     # print(  [* dicRetrieve [temporario[tamanho]],  nums[temporario[tamanho]]]  )
#     # # print(result_list)


# def longest_consecutive_sequence(nums):
#     num_set = set(nums)
#     longest_sequence = 0
    
#     for num in nums:
#         if num - 1 not in num_set:
#             current_num = num
#             current_sequence = 1
            
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_sequence += 1
            
#             longest_sequence = max(longest_sequence, current_sequence)
    
#     return longest_sequence


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0

    for num in nums:
        #start da sequencia
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1        

        #verificando se o proximo da sequencia está no set
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
        
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""