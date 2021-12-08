#!/usr/bin/env python3

class HydroVent(object):
    def __init__(self, line_endpoints, should_register_diag_line = False):
        self.point_to_vent_count = {}

        for endpoints in line_endpoints:
            x1, y1 = endpoints[0]
            x2, y2 = endpoints[1]
            if x1 == x2:
                self.register_vertical_line(endpoints)
            elif y1 == y2:
                self.register_horizontal_line(endpoints)
            elif should_register_diag_line:
                self.register_diag_line(endpoints)

    def register_vertical_line(self, endpoints):
        x1, y1 = endpoints[0]
        x2, y2 = endpoints[1]
        max_y = max(y1, y2)
        min_y = min(y1, y2)
        while min_y <= max_y:
            if (x1, min_y) in self.point_to_vent_count:
                self.point_to_vent_count[(x1, min_y)] += 1
            else:
                self.point_to_vent_count[(x1, min_y)] = 1
            min_y += 1

    def register_horizontal_line(self, endpoints):
        x1, y1 = endpoints[0]
        x2, y2 = endpoints[1]
        max_x = max(x1, x2)
        min_x = min(x1, x2)
        while min_x <= max_x:
            if (min_x, y1) in self.point_to_vent_count:
                self.point_to_vent_count[(min_x, y1)] += 1
            else:
                self.point_to_vent_count[(min_x, y1)] = 1
            min_x += 1

    def register_diag_line(self, endpoints):
        x1, y1 = endpoints[0]
        x2, y2 = endpoints[1]
        slope = (y2 - y1) / (x2 - x1)
        x_increment = 1
        y_increment = 1 if slope > 0 else -1
        leftmost_endpoint = (x1, y1) if (x1 < x2) else (x2, y2)
        rightmost_endpoint = (x1, y1) if (x1 > x2) else (x2, y2)
        while True:
            if (leftmost_endpoint) in self.point_to_vent_count:
                self.point_to_vent_count[leftmost_endpoint] += 1
            else:
                self.point_to_vent_count[leftmost_endpoint] = 1
            if leftmost_endpoint == rightmost_endpoint:
                break
            leftmost_endpoint = (leftmost_endpoint[0] + x_increment, \
                                 leftmost_endpoint[1] + y_increment)

    def count_overlapped_points(self):
        overlapped_points = 0

        for point in self.point_to_vent_count.keys():
            if self.point_to_vent_count[point] > 1:
                overlapped_points += 1

        return overlapped_points


