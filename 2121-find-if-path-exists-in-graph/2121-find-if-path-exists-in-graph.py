from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen=set()
        seen.add(source)
        D=defaultdict(list)
        for v,u in edges:
            D[u].append(v)
            D[v].append(u)
        
        def dfs_recursive(node):
          for nei_node in D[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                dfs_recursive(nei_node)
        dfs_recursive(source)
        return destination in seen