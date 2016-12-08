from itertools import product
from random import choice


class Field:
    def __init__(self, dim, size, rule, heat_map=False):
        self.heat_map = heat_map
        self.dim = dim
        self.size = size
        self.rule = rule
        self.active_cells = {}
        if heat_map:
            self.heat_cells = {}
        for cell in product([x for x in range(size)], repeat=dim):
            rand_cell = choice([0, 1])
            # self.cells[cell] = rand_cell
            if rand_cell:
                self.active_cells[cell] = 1
                if heat_map:
                    self.heat_cells[cell] = 0.1

    def get_around_cells(self, cell):
        for coordinate in product(range(-1, 2), repeat=self.dim):
            if any(coordinate):
                offset = tuple(map(sum, zip(cell, coordinate)))
                if all(map(lambda coord: coord < self.size and coord >= 0, offset)):
                    yield offset

    def update(self):
        new_active_cells = dict() # creating new dict for writing sum
        for active_cell in self.active_cells:
            # print("{}:".format(active_cell))
            for coordinate in self.get_around_cells(active_cell):
                # print(" {}".format(coordinate))
                if coordinate in new_active_cells:
                    # print(active_cell, 'activates', coordinate)
                    new_active_cells[coordinate] += 1
                else:
                    # print(active_cell, 'activates', coordinate)
                    new_active_cells[coordinate] = 1 # writing sum
        # print(new_active_cells)
        finally_active_cells = dict() # creating final dict with final cells
        for new_active_cell in new_active_cells:
            if new_active_cells[new_active_cell] == self.rule[1]:
                finally_active_cells[new_active_cell] = 1
                if self.heat_map:
                    if new_active_cell not in self.heat_cells:
                        self.heat_cells[new_active_cell] = 1
            else:
                if (new_active_cells[new_active_cell] == self.rule[0]) and (new_active_cell in self.active_cells):
                    finally_active_cells[new_active_cell] = 1 # rule in action
                    if self.heat_map:
                        if new_active_cell not in self.heat_cells:
                            self.heat_cells[new_active_cell] = 1

        self.active_cells = finally_active_cells # final cells now is active

        if self.heat_map:
            new_heat_cells = {} # creating new dict for heat
            for heat_cell in self.heat_cells:
                if heat_cell in self.active_cells:
                    new_heat_cells[heat_cell] = 1
                else:
                    self.heat_cells[heat_cell] -= 0.02
                    if self.heat_cells[heat_cell] > 0:
                        new_heat_cells[heat_cell] = self.heat_cells[heat_cell]
            self.heat_cells = new_heat_cells # final heat now is active

    def print_field(self): # just fancy filed printing
        for indy in range(self.size):
            for indx in range(self.size):
                if (indx, indy) in self.active_cells:
                    print("1 ", end='')
                else:
                    print("0 ", end='')
            print()
        print()