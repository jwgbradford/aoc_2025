with open('day_2_test.txt') as my_file:
    data : list[str] = my_file.read().split(',')

invalid_id_total : int = 0

for id_range in data:
    id_lower, id_upper = id_range.split('-')
    for id in range(int(id_lower), int(id_upper)+1):
        id_str = str(id)
        #if len(id_str) % 2 == 0:
        #if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
        #    invalid_id_total += id
        #    print(f"Invalid ID found: {id_str}")
        seg_length = 1
        for seg in range(0, len(id_str)-1):
            if id_str[seg] == id_str[seg + 1]:
                invalid_id_total += id
                print(f"Invalid ID found: {id_str}")
                break
print(invalid_id_total)