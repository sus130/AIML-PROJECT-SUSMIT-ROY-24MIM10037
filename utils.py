def manhattan_distance(position1, position2):
	row1, column1 = position1
	row2, column2 = position2
	return abs(row1 - row2) + abs(column1 - column2)

def print_grid_with_path(grid, path, start_node, goal_node):
	if not path:
		return
		
	grid_copy = []
	for grid_row in grid:
		new_row = []
		for cell in grid_row:
			new_row.append(cell)
		grid_copy.append(new_row)
	
	for position in path:
		if position != start_node and position != goal_node:
			row, column = position
			grid_copy[row][column] = '*'
			
	start_row, start_column = start_node
	grid_copy[start_row][start_column] = 'S'
	goal_row, goal_column = goal_node
	grid_copy[goal_row][goal_column] = 'G'
	
	for row_to_print in grid_copy:
		print(" ".join(row_to_print))
