def load_map_data(file_path):
	grid_layout = []
	dynamic_obstacle_schedule = {}
	start_position = None
	goal_position = None
	
	with open(file_path, 'r') as map_file:
		file_lines = map_file.read().splitlines()

	separator_index = -1
	for index, line in enumerate(file_lines):
		if line == '---':
			separator_index = index
			break
	
	grid_lines = file_lines
	obstacle_lines = []
	if separator_index != -1:
		grid_lines = file_lines[0:separator_index]
		obstacle_lines = file_lines[separator_index + 1:]

	for row_index, line_text in enumerate(grid_lines):
		row = []
		for column_index, char in enumerate(line_text):
			if char == 'S':
				start_position = (row_index, column_index)
				row.append('1')
			elif char == 'G':
				goal_position = (row_index, column_index)
				row.append('1')
			elif char == '.':
				row.append('1')
			else:
				row.append(char)
		grid_layout.append(row)
			
	for line_text in obstacle_lines:
		parts = line_text.split(',')
		position = (int(parts[1]), int(parts[2]))
		times = [int(time_str) for time_str in parts[3:]]
		for time in times:
			if time not in dynamic_obstacle_schedule:
				dynamic_obstacle_schedule[time] = []
			dynamic_obstacle_schedule[time].append(position)

	return grid_layout, dynamic_obstacle_schedule, start_position, goal_position

def get_terrain_cost(grid, position):
	row, column = position
	char_at_position = grid[row][column]
	if char_at_position.isdigit():
		return int(char_at_position)
	return 1

def is_valid_move(grid, position):
	row, column = position
	grid_height = len(grid)
	grid_width = len(grid[0])
	
	is_inside_bounds = (0 <= row < grid_height and 0 <= column < grid_width)
	if not is_inside_bounds:
		return False

	is_static_obstacle = (grid[row][column] == 'X')
	if is_static_obstacle:
		return False
		
	return True

def is_safe_at_time(position, time, dynamic_obstacle_schedule):
	if time in dynamic_obstacle_schedule:
		if position in dynamic_obstacle_schedule[time]:
			return False
	return True

def get_neighbors(position):
	row, column = position
	return [
		(row - 1, column), # up
		(row + 1, column), # down
		(row, column - 1), # left
		(row, column + 1), # right
	]
