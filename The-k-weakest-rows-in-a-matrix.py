import string
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp=[]
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j]==0:
                    if i not in temp:
                        temp.append(i)
                        
        for i in range(len(mat)):
            if i not in temp:
                temp.append(i)
        
        return(temp[0:k])
