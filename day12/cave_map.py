#!/usr/bin/env python3

class CaveMap(object):
    def __init__(self, edge_list):
        self.edge_map = {}
        self.end_paths = set()

        for edge in edge_list:
            start_node, end_node = edge
            if start_node in self.edge_map:
                self.edge_map[start_node].append(end_node)
            else:
                self.edge_map[start_node] = [end_node]
            if end_node in self.edge_map:
                self.edge_map[end_node].append(start_node)
            else:
                self.edge_map[end_node] = [start_node]

    def compute_end_paths(self, can_visit_small_cave_twice = False):
        cave_path = []
        visited_caves = set()
        self.dfs('start', cave_path, visited_caves, can_visit_small_cave_twice)

    def dfs(self, current_node, cave_path, visited_caves,
            can_visit_small_cave_twice = False, visited_small_cave_twice = False):
        new_cave_path = cave_path.copy()
        new_visited_caves = visited_caves.copy()
        new_cave_path.append(current_node)
        new_visited_caves.add(current_node)

        if current_node == 'end':
            self.end_paths.add(tuple(new_cave_path))
            return

        for adjacent_cave in self.edge_map[current_node]:
            if adjacent_cave.isupper():
                self.dfs(adjacent_cave, new_cave_path, new_visited_caves,
                         can_visit_small_cave_twice, visited_small_cave_twice)
            elif not adjacent_cave in new_visited_caves:
                self.dfs(adjacent_cave, new_cave_path, new_visited_caves,
                         can_visit_small_cave_twice, visited_small_cave_twice)
            elif can_visit_small_cave_twice and (not visited_small_cave_twice) \
                 and not (adjacent_cave in ['start', 'end']):
                self.dfs(adjacent_cave, new_cave_path, new_visited_caves,
                         can_visit_small_cave_twice, True)

    def get_num_end_paths(self):
        return len(self.end_paths)

    def print_end_paths(self):
        print(self.end_paths)

