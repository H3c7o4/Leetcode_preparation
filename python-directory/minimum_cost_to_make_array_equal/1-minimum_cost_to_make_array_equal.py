#!/usr/bin/env python3
"""
Given two 0-indexed arrays nums and cost consisting each of
n positive integers.
You can do the following operation any number of times:
    - Increase or decrease any element of the array nums by 1
The cost of doing one operation on the ith element is cost[i]
The function must Return the minimum total cost such that all the elements
of the array nums become equal.
"""


class Solution(object):
    """Implement the first solution """
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(nums)
        cost_list = []
        allEqual = all(x == nums[0] for x in nums)

        if allEqual:
            return 0
        else:
            for i in range(n):
                comp = nums[i]
                localcost = 0
                for j in range(n):
                    coef = cost[j]
                    ops = abs(nums[j] - comp)
                    localcost = localcost + (coef * ops)
                cost_list.append(localcost)
            minicost = min(cost_list)
            return minicost
