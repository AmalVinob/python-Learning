# # def selection_sort(arr):
# #     n = len(arr)
# #     for i in range(n):
# #         # Find the minimum element in the remaining unsorted array
# #         min = i
# #         for j in range(i + 1, n):
# #             if arr[j] < arr[min]:
# #                 min = j
# #
# #         # Swap the found minimum element with the first element
# #         arr[i], arr[min] = arr[min], arr[i]
# #
# #     return arr
# #
# #
# # # Example usage
# # numbers = [64, 25, 12, 22, 11]
# # sorted_numbers = selection_sort(numbers)
# # print("Sorted array:", sorted_numbers)
# #
#
# # arr = [1,2,2,3,4,5,6]
# # arr = array(arr)
#
# # n = len(arr)
# # unique_value = 0
# # for i in range(0,n):
# #     for j in range(i+1,n):
# #         if arr[i] == arr[j]:
# #             unique_value = i
# # if unique_value == 0:
# #     print("there is no unique value")
# # else:
# #     print(f"the unique value is {unique_value}")
#
# # print(type(arr))
# import numpy as np
# arr = np.array([1,2,4,3,4,5])
# n = len(arr)
# unique_value = 0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             unique_value = j
# if unique_value == 0:
#     print("there is no unique value")
# else:
#     print(f"the unique value is {unique_value}")
#



def facto(n):
    if n==0:
        return 1
    else:
        return n * facto(n-1)

print(facto(5))
