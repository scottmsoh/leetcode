

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ran = Counter(ransomNote)
        count_mag = Counter(magazine)
        
        for ran in count_ran:  
            if count_ran[ran] > count_mag[ran]:
                return False
        return True
