class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = collections.defaultdict(list)
        for src, dist in edges:
            reachable[dist].append(src)
        
        res = []
        for i in range(n):
            if not reachable[i]:
                res.append(i)
        return res

        
        
