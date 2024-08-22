# """
# This problem revolves around understanding the concept of "safe nodes" in a directed graph. The graph is made up of nodes connected by directed edges, where each node may point to one or more other nodes.

# Key Concepts:
# Directed Graph: This is a type of graph where edges have a direction, meaning an edge from node A to node B doesn't imply there is an edge from B to A.

# Terminal Node: A terminal node is a node that has no outgoing edges. In simpler terms, once you reach a terminal node, there are no further paths to follow.

# Safe Node: A node is considered safe if every possible path you can take from that node leads to a terminal node. This means there’s no way to enter an infinite loop or cycle starting from a safe node.

# Task:
# You are given a graph, and your goal is to identify all the safe nodes in the graph. The problem requires you to return these nodes sorted in ascending order.

# Example 1 Explanation:
# Consider the graph [[1,2],[2,3],[5],[0],[5],[],[]]:

# Nodes 5 and 6 are terminal nodes because they have no outgoing edges.
# Node 2 can only lead to nodes 5 and 6, which are terminal nodes, so node 2 is safe.
# Node 4 also only leads to a terminal node (node 5), so it is safe.
# Thus, the safe nodes in this graph are [2, 4, 5, 6].

# Example 2 Explanation:
# In the graph [[1,2,3,4],[1,2],[3,4],[0,4],[]]:

# Node 4 is the only terminal node.
# All paths starting from node 4 lead to node 4 itself, making it the only safe node.
# So, the safe node here is [4].

# The challenge is to identify these safe nodes by analyzing the graph structure and understanding how paths flow through the nodes.
# """

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hm = {i:[] for i in range(len(graph))}
        for i, l in enumerate(graph):
            hm[i] = l
        
        seen = set()
        cache = {}
        def dfs(node):
            if node in seen:
                return False
            if node in cache:
                return cache[node]
            if hm[node] == []:
                return True
            
            seen.add(node)

            for n in hm[node]:
                if not dfs(n):
                    cache[n] = False
                    return cache[n]
            cache[node] = True
            seen.remove(node)
            return cache[node]
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
    
    # Time complexity --> O(V+E)
    # Topological sort