class Solution:
    def maxArea(self, height):
        left=0
        right=len(height)-1
        volume=0
        while left!=right:
            temp=(right-left)*min(height[right],height[left])
            if volume<temp:
                volume=temp
            if height[left]<=height[right]:left+=1
            else: right-=1
        return volume

