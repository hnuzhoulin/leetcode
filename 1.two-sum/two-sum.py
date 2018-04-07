#!/usr/bin/python
#! -*- encoding:utf-8 -*-

# Author:   Zhoulin
# FIle:     two-sum.py
# Role:     leetcode,return the two index of the list,which sum value equal the given number
# Created:  2018-04-27 21:19
# Modified:
#       2018-04-27 21:19 : first version
# ---------------------------------


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = []
        length = len(nums)
        for first in range(0,length):
            for second in range(first+1,length):
                if (nums[first] + nums[second] == target):
                    found.extend([first, second])
                    return found

def  main():
    nums = [2, 7, 11, 15]
    target = 9
    result = []
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result:
        print("%s" %result )
    else:
        print("Not Found")

if __name__ == '__main__':
    main()