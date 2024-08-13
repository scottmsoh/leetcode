

from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter_nums = Counter(nums) 
        
        for num in nums:
            if counter_nums[num] == 1: 
                return num
