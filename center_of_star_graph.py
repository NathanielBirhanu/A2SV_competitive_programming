class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = edges[0]
        m = edges[1]
        if n[0] == m[0] or n[0] == m[1]:
            return n[0]
        else:
            return n[1]
        

        
