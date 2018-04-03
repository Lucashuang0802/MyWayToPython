from collections import defaultdict

class DFS_Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        res = []
        self.dfs_helper(s, res, [False] * len(self.graph))
        return res

    def dfs_helper(self, s, res, visited):
        visited[s] = True
        res.append(s)

        for obj in self.graph[s]:
            if visited[obj] != True:
                self.dfs_helper(obj, res, visited)


if __name__ == "__main__":
    # Driver code
    # Create a graph given in the above diagram
    g = DFS_Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.dfs(2))
