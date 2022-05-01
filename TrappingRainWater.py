# author: yprakash
# https://leetcode.com/problems/trapping-rain-water/
# https://leetcode.com/submissions/detail/690878848/

class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        water = 0
        leftp = 0  # Initialize left, right pointers to extreme ends
        rightp = len(height) - 1
        max_left = 0  # Max value seen to leftside of current position we proceed
        max_right = 0  # right side max

        while leftp < rightp:
            # decide which side we need to operate on
            if height[leftp] <= height[rightp]:  # Operate on left side index
                if max_left < height[leftp]:  # We can't trap water on it in any case
                    max_left = height[leftp]
                else:
                    water += max_left - height[leftp]  # trap water
                leftp += 1

            else:  # Operate on right side index
                if max_right < height[rightp]:
                    max_right = height[rightp]
                else:
                    water += max_right - height[rightp]
                rightp -= 1

        return water
