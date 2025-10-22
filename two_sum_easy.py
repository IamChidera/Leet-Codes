# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:47:51 2025

@author: bless
"""

#TwoSum (given a target number to loop through a list and give an output of the two numbers that add up to the target)
#Easy (loop through list)
def two_sum (num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return [i, j] 

num = [2, 7, 11, 15]
target = 9
two_sum (num, target)

#Time: O(n²)
#Space: O(1)


#Best(hash maps/dictionary)
def Two_Sum (nums, target):
    lookup = {}
    for i, nums in enumerate (nums):
        complement = target - nums
        if complement in lookup:
            return[lookup[complement], i]
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

#Time: O(n)
#Space: O(n)