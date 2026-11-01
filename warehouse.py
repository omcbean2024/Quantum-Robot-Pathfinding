# Warehouse grid, shelves, obstacles

# warehouse size
ROWS = 12
COLS = 12

# Warehouse code grid
# 0 - open space
# 1 - obstacle
# 2 - charging station

warehouse = []
for i in range(ROWS):
    current_row = []
    for j in range(COLS):
        warehouse_grid_spot = 0
        current_row.append(warehouse_grid_spot)
    warehouse.append(current_row)

#obstacles
warehouse[4][6] = 1
warehouse[4][7] = 1
warehouse[4][8] = 1

# charging stations
warehouse[11][5] = 2
warehouse[11][6] = 2
warehouse[11][7] = 2

robot_1 = [10, 5]
robot_2 = [10, 6]
robot_3 = [10, 7]

#robot 1 position
robot_1_row = robot_1[0]
robot_1_column = robot_1[1]

#robot 2 position
robot_2_row = robot_2[0]
robot_1_column = robot_1[1]

#robot 3 position
robot_3_row = robot_3[0]
robot_1_column = robot_1[1]

robot_1_task_destination = [1, 1]
robot_2_task_destination = [8, 3]
robot_3_task_destination = [1, 10]

for row in warehouse:
    for cell in row:
        if cell == 0:
            print(".", end=" ")
        elif cell == 1:
            print("#", end=" ")
        elif cell == 2:
            print("C", end=" ")
        
    print()
# for row in warehouse:
    #print(row)


