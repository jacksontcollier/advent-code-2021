#!/usr/bin/env python3

class HeightMap(object):
    def __init__(self, height_map_matrix):
        self.height_map_matrix = height_map_matrix
        self.height = len(self.height_map_matrix)
        self.width = len(self.height_map_matrix[1])

    def get_low_point_locations(self):
        low_point_locations = []
        for i, height_map_row in enumerate(self.height_map_matrix):
            for j, height in enumerate(height_map_row):
                adjacent_heights = self.get_adjacent_heights(i, j)
                if height < min(adjacent_heights):
                    low_point_location = (i, j)
                    low_point_locations.append(low_point_location)

        return low_point_locations

    def get_adjacent_heights(self, row_i, col_i):
        adjacent_locations = [
            (row_i-1, col_i),
            (row_i, col_i+1),
            (row_i+1, col_i),
            (row_i, col_i-1)
        ]
        is_loc_in_range = lambda loc: loc[0] >= 0 and loc[0] < self.height \
                                      and loc[1] >= 0 and loc[1] < self.width
        adjacent_locations = filter(is_loc_in_range, adjacent_locations)
        adjacent_heights = []
        for location in adjacent_locations:
            row_i, col_i = location
            adjacent_heights.append(self.height_map_matrix[row_i][col_i])

        return adjacent_heights

    def get_low_point_risk(self):
        low_point_locations = self.get_low_point_locations()
        low_point_heights = [self.height_map_matrix[loc[0]][loc[1]] for loc in \
                             low_point_locations]
        total_risk = 0
        for height in low_point_heights:
            total_risk += height+1

        return total_risk

