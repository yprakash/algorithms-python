# Given an array of integers nums and an integer target, return two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, nums won't have repeat integers, and you may not use the same element twice.

class PairSumUnique:
    def pairSum(self, nums: List[int], target: int) -> List[int]:
        # Returns two unique values in numbers whose sum is target
        return next((i, j) for i in nums for j in nums if i+j == target and i != j)
