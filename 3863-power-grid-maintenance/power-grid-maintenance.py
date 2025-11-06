"""
Solution Priority Queue + hashmap.


Let operational be a mapping where operational[c] is true if power station c is operational, and false otherwise.
Let components be a mapping where if components[c] = x, then power station c is in component x.
Let queues be a mapping where queues[c] points to the priority queue (min heap) that consists of all the nodes (operational or not)
of the component which node c is in ascending order by ID.

First, we draw the graph, and map each node to its component.



On a [2, x] query, we declare power station x inoperable by setting operational[c] = false.

On a [1, x] query, 
    we check if operational[x] = True, if so, return x,
    If not, keep deleting top of the min heap queues[x] until the top has a node that is operational,
    or the queue is empty. Return the top of the queue, or if -1 the heap is empty.
"""

from collections import deque
import heapq
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:


        def bfs(u, comp_no, heap):
            queue = deque([u])

            while queue:
                u = queue.popleft()

                components[u] = comp_no
                heapq.heappush(heap, u)

                for v in graph[u]:
                    if components[v] == -1:
                        queue.append(v)





        #All nodes are operational initially
        operational = [True] * ( c + 1)

        #Map each node to the component it belongs to
        components = [-1] * (c + 1)

        #Draw the graph
        graph = {x:[] for x in range(1, c+1)}
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        comp_no = 0


        queues = []
        for u in range(1, c+1):
            if components[u] == -1:
                component = []
                bfs(u,comp_no, component)
                queues.append(component)
                comp_no += 1

        
        ret = []
        for (type_, node) in queries:
            if type_ == 2:
                operational[node] = False

            
            elif operational[node]:
                ret.append(node)
            
            else:
                comp = components[node]

                while queues[comp]:
                    top =heapq.heappop(queues[comp])

                    if operational[top]:
                        ret.append(top)
                        heapq.heappush(queues[comp], top)
                        break
                    

                if not queues[comp]:
                    ret.append(-1)
            
        return ret


        