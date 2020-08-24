def earliest_ancestor(ancestors, starting_node):
    # create the graph
    graph = {}
    # create all of the vertices
    for i in range(len(ancestors)):
        # add edge cases
        graph[i] = set(ancestors[i])
    # print(graph)

    # the stack
    stack = []
    stack.append([starting_node])

    compare = [] # all completed arrays

    current_vert = starting_node
    visited = set()

    # at this point, stack has one list w/one item
    while len(stack) != 0:
        current_list = stack.pop() # grab top list
        print(current_list, "IN FIRST")
        current_vert = current_list.pop() # current vert is last item in list

        if current_vert not in visited:
            current_list.append(current_vert) # add item back to list

        visited.add(current_vert) # add to visited

        try:
            neighbors = graph[current_vert] # grab neighbors
        except:
            neighbors = []

        if len(neighbors) < 1:
            print(current_list, "IN IF")
            compare.append(current_list) # if no neighbors, list is done, append to compare
        else:
            for num in neighbors:
                new_list = current_list + [num] # make a new path for each neighbor
                stack.append(new_list) # add new list to stack to be evaluated

    # print(compare, "COMPARE LIST")


# erase below
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)
