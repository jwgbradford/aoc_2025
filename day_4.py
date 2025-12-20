def get_adjacent_cells(r_coord, c_coord) -> int:
    result = 0
    #print(f'r_coord : {r_coord} c_coord : {c_coord}')
    for r,c in [(r_coord+i,c_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if is_roll(r, c):
            #print(f'  row : {r} column : {c}')
            result += 1
    return result

def is_roll(r, c):
    if r < 0 or c < 0 or r > row_length -1  or c > column_length - 1: # assume each row same len
        return False
    if data_map[r][c] == '@':
        return True
    return False

with open('day_4_input.txt') as file:
    data = file.read().split()
#print(data)

data_map = []

for row in data:
    data_map.append(list(row))
row_length = len(data_map)
column_length = len(data_map[0])

#print(data_map)

roll_count = 0
remove_more = True
while remove_more:
    remove_more = False
    for r in range(row_length):
        for c in range(column_length):
            if data_map[r][c] == '@':
                if get_adjacent_cells(r, c) < 4:
                    data_map[r][c] = '.'
                    roll_count += 1
                    remove_more = True


print(roll_count)
