class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = []
        for i in set(s):
            print(i)
            if s.count(i) == 1:
                unique.append(s.index(i))
                print(unique)
        if len(unique) == 0:
            return -1  
        else:
            return min(unique)
            
