from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # create the graph
    graph = Graph()

    for item in ancestors:
        parent = item[0]
        child = item[1]

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)

    ancestral_path = []
    for i in graph.vertices:
        result = graph.dfs(i, starting_node)

        if result is not None:
            if len(result) > len(ancestral_path):
                ancestral_path = result
            elif len(result) == len(ancestral_path):
                if result[-1] < ancestral_path[-1]:
                    ancestral_path = result


    if ancestral_path[0] == starting_node:
        return -1
    else:
        return ancestral_path[0]
