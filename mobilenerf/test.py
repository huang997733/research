import numpy as np
import pandas as pd

grid_dtype = np.float32
point_grid_size = 128

#plane parameter grid
point_grid = np.zeros(
      (point_grid_size, point_grid_size, point_grid_size, 3),
      dtype=grid_dtype)

point_grid = np.zeros(
      (point_grid_size, point_grid_size, point_grid_size, 3),
      dtype=grid_dtype)
acc_grid = np.zeros(
      (point_grid_size, point_grid_size, point_grid_size),
      dtype=grid_dtype)
point_grid_diff_lr_scale = 16.0/point_grid_size

print(point_grid.shape)
print(acc_grid.shape)
print(point_grid_diff_lr_scale)
