#!/usr/bin/env python
# coding: utf8

import sys, os
import unittest
import numpy as np

sys.path.insert(0, os.path.dirname(__file__) + "../")

from kernel.td_kernel_dmvw import TDKernelDMVW

# Set parameters
min_x = 0
min_y = 0
max_x = 10
max_y = 5
cell_size = 1
kernel_size = 10 * cell_size
wind_scale = 0.05
time_scale = 0.001
evaluation_radius = 10*kernel_size

number_of_x_cells = int(round((max_x - min_x) / cell_size + 1, 0))
number_of_y_cells = int(round((max_y - min_y) / cell_size + 1, 0))

class TestCellGridContent(unittest.TestCase):

    def setUp(self):
        self.kernel = TDKernelDMVW(min_x, min_y, max_x, max_y, cell_size, kernel_size, wind_scale, time_scale, low_confidence_calculation_zero=True, evaluation_radius=evaluation_radius)

    def testCellGridShape(self):
        self.assertEqual(number_of_x_cells, self.kernel.cell_grid_x.shape[0])
        self.assertEqual(number_of_x_cells, self.kernel.cell_grid_y.shape[0])
        self.assertEqual(number_of_y_cells, self.kernel.cell_grid_x.shape[1])
        self.assertEqual(number_of_y_cells, self.kernel.cell_grid_y.shape[1])

    def testCellGridXContent(self):
        for x_idx in range(number_of_x_cells):
            for y_idx in range(number_of_y_cells):
                # In the x grid, the cells are defined by the x_idx and do not depend on the y_idx
                self.assertEqual(min_x + (x_idx * cell_size), self.kernel.cell_grid_x[x_idx][y_idx])

    def testCellGridYContent(self):
        for x_idx in range(number_of_x_cells):
            for y_idx in range(number_of_y_cells):
                # In the y grid, the cells are defined by the y_idx and do not depend on the x_idx
                self.assertEqual(min_y + (y_idx * cell_size), self.kernel.cell_grid_y[x_idx][y_idx])
            
if __name__ == '__main__':
    unittest.main()
