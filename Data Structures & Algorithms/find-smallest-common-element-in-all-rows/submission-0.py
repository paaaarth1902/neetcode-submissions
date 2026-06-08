class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        mySet = set(mat[0])
        # print(mat[0])

        for row in mat[1:]:
            mySet = mySet & set(row)
        
        if len(mySet) <= 0:
            return -1
        
        result = sorted(list(mySet))[0]
        return result
