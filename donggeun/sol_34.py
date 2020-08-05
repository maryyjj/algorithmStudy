class Solution:
    def searchRange(self, nums,target):
        result = []
        cnt = 0
        start = 0
        end = 0
        while True:
            if target in nums:
                if cnt != 0:
                    end = nums.index(target)+cnt
                else:
                    start = nums.index(target)
                    end = nums.index(target)
                nums.remove(target)
                cnt+=1

            if target not in nums:
                if cnt == 0:
                    result.append(-1)
                    result.append(-1)
                    break
                else:
                    result=[start,end]
                    break
        return result