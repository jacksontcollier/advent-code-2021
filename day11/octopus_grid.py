#!/usr/bin/env python3

import pdb
from queue import Queue

class OctopusGrid(object):
    def __init__(self, grid):
        self.grid = grid
        self.energy_level_threshold = 9
        self.num_flashes = 0
        self.synchronization_step = None

    def get_num_flashes(self):
        return self.num_flashes

    def get_synchronization_step(self):
        return self.synchronization_step

    def get_adjacent_pos(self, x, y):
        adjacent_pos = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        filter_adjacent_pos = lambda pos: pos[0] >= 0 \
                and pos[0] < len(self.grid) and pos[1] >= 0 \
                and pos[1] < len(self.grid[0])
        adjacent_pos = list(filter(filter_adjacent_pos, adjacent_pos))

        return adjacent_pos

    def synchronize(self):
        step = 0
        while not self.is_synchronized():
            self.simulate_step(step)
            step += 1
        self.synchronization_step = step

    def simulate_nsteps(self, n):
        for step in range(n):
            self.simulate_step(step)

    def simulate_step(self, step):
        pending_flash_pos = Queue()
        flash_pos_set = set()

        for i, row in enumerate(self.grid):
            for j, energy_level in enumerate(row):
                self.grid[i][j] += 1
                if self.grid[i][j] > self.energy_level_threshold:
                    octopus_pos = (i, j)
                    pending_flash_pos.put(octopus_pos)
                    flash_pos_set.add(octopus_pos)

        while not pending_flash_pos.empty():
            flash_pos = pending_flash_pos.get()
            x, y = flash_pos
            adjacent_pos = self.get_adjacent_pos(x, y)

            for pos in adjacent_pos:
                if pos not in flash_pos_set:
                    self.grid[pos[0]][pos[1]] += 1
                    if self.grid[pos[0]][pos[1]] > self.energy_level_threshold:
                        pending_flash_pos.put(pos)
                        flash_pos_set.add(pos)

            self.num_flashes += 1
            self.grid[x][y] = 0

    def is_synchronized(self):
        val = self.grid[0][0]

        for row in self.grid:
            for energy_level in row:
                if energy_level != val:
                    return False

        return True

