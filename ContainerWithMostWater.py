# author: yprakash
# https://leetcode.com/problems/container-with-most-water/
# https://leetcode.com/submissions/detail/690408370/

class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i, j = 0, len(height)-1

        while i < j:
            if height[i] < height[j]:
                newArea = (j-i) * height[i]
                i += 1
            else:
                newArea = (j-i) * height[j]
                j -= 1
            if maxArea < newArea:
                maxArea = newArea
        return maxArea
