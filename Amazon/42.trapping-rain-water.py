#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        waterTrapped = 0
        lenght = len(height)
        if lenght<1:
            return waterTrapped
        leftIndex = 0
        rightIndex = lenght-1
        leftMax = 0
        rightMax = 0
        
        while leftIndex<rightIndex:
            leftHeight = height[leftIndex]
            rightHeight = height[rightIndex]
            if leftHeight < rightHeight:
                if leftMax<leftHeight:
                    leftMax = leftHeight
                leftIndex+=1
                waterTrapped += (leftMax-leftHeight)
            else:
                if rightMax<rightHeight:
                    rightMax = rightHeight
                waterTrapped += (rightMax-rightHeight)
                rightIndex-=1
        return waterTrapped

        
# @lc code=end

