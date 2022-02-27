class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = list(map(len, strs))
        print(length)
        
        small = min(length)
        index = length.index(min(length))
        
        i = 0
        while i < small:
            for j in range(len(strs)):
                if strs[index][i] != strs[j][i]:
                    return strs[0][:i]
            i+=1
            
        return strs[0][:i]
