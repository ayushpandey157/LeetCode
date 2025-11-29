class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.count = 0 # you can also use nonlocal within below dfs function
        
        def sumtree(node, parent):
            s = values[node]
            for child in graph[node]:
                if not child == parent:
                    s += sumtree(child, node)
            
            self.count += (s%k==0)
            return s
        
        sumtree(0, None)
        return self.count