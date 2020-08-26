from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # find vertex v1, add v2 to the set
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

        while queue.size() > 0:
            current = queue.dequeue()

            if current not in visited:
                print(current)
                visited.add(current)

                for i in self.get_neighbors(current):
                    queue.enqueue(i)

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current = stack.pop()

            if current not in visited:
                print(current)
                visited.add(current)

                for i in self.get_neighbors(current):
                    stack.push(i)

    def dft_recursive(self, starting_vertex, visited=set()):
        # depth first, recursive
        visited.add(starting_vertex)
        print(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        for n in neighbors:
            if n not in visited:
                self.dft_recursive(n, visited)


    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        visited = set()
        queue.enqueue({
            'current_vert': starting_vertex,
            'path': [starting_vertex]
        })

        while queue.size() > 0:
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vert = current_obj['current_vert']

            if current_vert not in visited:

                if current_vert == destination_vertex:
                    print(current_path)
                    return current_path

                visited.add(current_vert)

                for neighbor_vert in self.get_neighbors(current_vert):
                    new_path = list(current_path)
                    new_path.append(neighbor_vert)

                    queue.enqueue({
                        'current_vert': neighbor_vert,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        stack = []
        visited = set()
        stack.append([starting_vertex])

        while len(stack) > 0:
            current_path = stack.pop()
            current = current_path[-1]

            if current == destination_vertex:
                return current_path

            visited.add(current)

            for vert in self.get_neighbors(current):
                new_stack = list(current_path)
                new_stack.append(vert)

                stack.append(new_stack)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=list()):
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        # loop through all verticies
        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                # path.append(vert)
                new_path = self.dfs_recursive(vert, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
