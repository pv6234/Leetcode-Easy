class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0

        for i in s[::-1]:
            if i!=' ':
                c+=1
            if i==' ' and c!=0:
                break
        return c
            
