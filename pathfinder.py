def printPath(stack):
    for i in range(len(stack) - 1):
        print(stack[i], end=" -> ")
    print(stack[-1])


# Graph class with breadth first search and depth first search
# algorithms implemented to find the longest path of graph
# graph implemented in undirected
class Graph:

    # Constructor Method
    # Parameters:
    #   vertices -> number of vertices in graph
    # Globals:
    #   vertices -> number of vertices in graph
    #   graph -> edge set
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(self.vertices)}
        self.cylce = False

    # Method to add edges to edge set
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Breadth first search implementation.
    # Parameters:
    #   node -> the current vertex
    def bfs(self, node):

        queue = []
        visited = [False for i in range(self.vertices + 1)]
        distance = [-1 for i in range(self.vertices + 1)]
        visited[node] = True
        queue.append(node)
        distance[node] = 0

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[s] + 1
                    queue.append(i)

        maxDistance = 0

        for i in range(self.vertices):
            if distance[i] > maxDistance:
                maxDistance = distance[i]
                node = i

        print("\n")
        print(maxDistance)
        return node, maxDistance

    # Depth first search implementation
    # Finds the vertices in the longest path
    # Parameters:
    #   visited -> what vertices have already been visited
    #   current -> current vertex dfs is on
    #   end -> end vertex of the path
    #   stack -> stack to track the path
    def dfs(self, visited, current, end, stack):
        # Add current to the path
        stack.append(current)
        if current == end:
            printPath(stack)
            return stack
        visited[current] = True

        if len(self.graph[current]) > 0:
            for next in self.graph[current]:

                # if the node is not visited
                if not visited[next]:
                    self.dfs(visited, next, end, stack)

        del stack[-1]

    def longestPath(self):
        stack = []
        longestNode = 0
        longestDistance = 0
        for i in range(self.vertices):
            if len(self.graph[i]) == 1:
                node, dist = self.bfs(i)
                if dist > longestDistance:
                    longestNode = i
                    longestDistance = dist

        node, LongDistance = self.bfs(longestNode)
        visited = [0 for i in range(self.vertices)]
        path = self.dfs(visited, longestNode, node, stack)
        print('Longest path is from', longestNode, 'to', node, 'of length', LongDistance)

        return path

    def cycleFinder(self):
        path = []
        path.append(self.longestPath())
        for i in range(len(path) - 1):
            visited = []
            self.dfsCycle(visited, path[i])

    def dfsCycle(self, visited, node):
        if node not in visited:
            visited.add(node)
            for next in self.graph[node]:
                self.dfsCycle(visited, next)
        elif node in visited:
            self.cylce = True


# Driver
G = Graph(10)
G.addEdge(0, 1)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(2, 9)
G.addEdge(2, 4)
G.addEdge(4, 5)
G.addEdge(1, 6)
G.addEdge(6, 7)
G.addEdge(6, 8)
G.cycleFinder()
print(G.cylce)
