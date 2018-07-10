# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {} #空的字典，keys-->values
        for i, num in enumerate(nums): #enumerate的用法
            if target - num in lookup.keys():
                return [lookup[target - num], i]
            lookup[num] = i

if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))


