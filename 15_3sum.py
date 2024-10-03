
https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i=0
        nums.sort()
        res = []

        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            target = -(nums[i])
            if i > 0 and nums[i] == nums[i-1]:
        #    if nums[i] == nums[j] and nums[k] == nums[i]:
                continue
            # j,k = i+1, len(nums)-1
            if k == i:
                break
            while j<k:
                summed = nums[j]+nums[k]
                if target == summed:
                    res.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif summed > target:
                    k-=1
                else:
                    j+=1
        return res
