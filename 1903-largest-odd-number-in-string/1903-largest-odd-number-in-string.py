class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        end = -1
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                end = i
        
        if end == -1:
            return ans
        else:
            return (num[:end+1])
        