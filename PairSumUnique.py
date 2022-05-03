# author: yprakash
# Given an array of integers nums and an integer target, return two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, nums won't have repeat integers, and you may not use the same element twice.
# https://leetcode.com/problems/two-sum
# https://leetcode.com/submissions/detail/692011049

class PairSumUnique:
    def pairSum(self, nums: List[int], target: int) -> List[int]:
        # Returns two unique values in numbers whose sum is target
        # O(n^2) solution in pythonic way
        # return next((i, j) for i in nums for j in nums if i+j == target and i != j)

        elems = {target-nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in elems:
                return [elems[nums[i]], i]
            elems[target-nums[i]] = i
        return None
