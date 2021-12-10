#!/usr/bin/env python3

class HeightMap(object):
    def __init__(self, height_map):
        self.height_map = height_map
        self.height = len(self.height_map)
        self.width = len(self.height_map[0])

    def get_low_points(self):
        low_points = []
        for i, height_map_row in enumerate(self.height_map):
            for j, height in enumerate(height_map_row):
                adjacent_heights = self.get_adjacent_heights(i, j)
                if height < min(adjacent_heights):
                    low_point = (i, j)
                    low_points.append(low_point)

        return low_points

    def get_adjacent_points(self, row_i, col_i):
        adjacent_points = [
            (row_i-1, col_i),
            (row_i, col_i+1),
            (row_i+1, col_i),
            (row_i, col_i-1)
        ]
        is_point_in_range = lambda point: point[0] >= 0 and point[0] < self.height \
                and point[1] >= 0 and point[1] < self.width
        adjacent_points = list(filter(is_point_in_range, adjacent_points))
        return adjacent_points

    def get_adjacent_heights(self, row_i, col_i):
        adjacent_points = self.get_adjacent_points(row_i, col_i)
        adjacent_heights = []
        for point in adjacent_points:
            row_i, col_i = point
            adjacent_heights.append(self.height_map[row_i][col_i])

        return adjacent_heights

    def get_low_point_risk(self):
        low_points = self.get_low_points()
        low_point_heights = [self.height_map[point[0]][point[1]] for point in \
                             low_points]
        total_risk = 0
        for height in low_point_heights:
            total_risk += height+1

        return total_risk

    def get_points_in_basin(self, low_point):
        basin_points = set([low_point])
        self.get_adjacent_basin_points(low_point, basin_points)
        return basin_points

    def get_adjacent_basin_points(self, point, basin_points):
        x , y = point
        adjacent_points = self.get_adjacent_points(x, y)
        point_height = self.height_map[x][y]
        for adjacent_point in adjacent_points:
            x, y = adjacent_point
            adjacent_point_height = self.height_map[x][y]
            if adjacent_point_height < 9 \
               and adjacent_point_height > point_height:
                basin_points.add(adjacent_point)
                self.get_adjacent_basin_points(adjacent_point, basin_points)

    def get_basins(self):
        low_points = self.get_low_points()
        basins = []
        for low_point in low_points:
            basins.append(self.get_points_in_basin(low_point))

        return basins

    def get_largest_basins_product(self):
        basins = self.get_basins()
        basin_sizes = [len(basin) for basin in basins]
        basin_sizes.sort(reverse=True)
        product = 1
        for basin_size in basin_sizes[:3]:
            product *= basin_size

        return product
