#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_set = (c for c in s1)
    s2_set = (d for d in s2)
    s1_list = list(s1_set)
    s2_list = list(s2_set)
    check_bool = None
    return s2_list

    for c in s1_list:
        # if len(s2_list) > 1000:
        #     if binary_search(c, s2_list):
        #         check_bool = True
        #         break
        if c in s2_list:
            check_bool = True
            break
        else:
            check_bool = False
    if check_bool:
        return 'YES'
    else:
        return 'NO'

# def binary_search(ans, arr):
#     bool_check = None
#     low = 0
#     high = len(arr) - 1
#     while low < high:
#         mid = (low + high) // 2
#         if ans == arr[mid]:
#             return True
#         elif ans in arr[:mid]:
#             high = mid + 1
#         elif ans in arr[mid:]:
#             low = mid - 1
#         else:
#             return False
#     return bool_check


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
