#!/usr/bin/env python3
from collections import deque
import os
from graphviz import Digraph


class Cave:
    def __init__(self, name, connections):
        pass


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    graph = {}
    for row in rows:
        a, b = row.split("-")
        if(b != "start"):
            if a in graph.keys():
                graph[a].add(b)
            else:
                graph[a] = {b}

        if(a != "start"):
            if b in graph.keys():
                graph[b].add(a)
            else:
                graph[b] = {a}
    graph["end"] = {}

    dot = Digraph()
    [dot.node(node, node) for node in graph.keys()]
    dot.edges([(key, subvalue) for key, value in graph.items()
              for subvalue in value])

    dot.render(os.path.join(dirname, '../part1/graph'), format="png")

    current_path = []
    paths = []
    frontier = deque()
    frontier.append(["start"])
    while frontier:
        current_path = frontier.popleft()
        last_node = current_path[len(current_path)-1]
        neighbours = graph[last_node]

        if last_node == "end":
            paths.append(current_path)

        visited_twice = False
        small_cave_count = [key for key in current_path if key.islower()]
        if(len(set(small_cave_count)) + 1 < len(small_cave_count)):
            # We've visited a small cave twice now
            visited_twice = True

        for neighbour in neighbours:
            if neighbour.isupper() or (neighbour.islower() and not visited_twice and len([node for node in current_path if node == neighbour]) < 2):
                frontier.append(current_path + [neighbour])

    print("")
    # [print(",".join(path)) for path in paths]
    print("Total paths: " + str(len(paths)))


if __name__ == "__main__":
    main()
