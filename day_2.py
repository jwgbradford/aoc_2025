with open('day_2_test.txt') as my_file:
    data : list[str] = my_file.read().split(',')

invalid_id_total : int = 0
print(data)

for id_range in data:
    id_lower, id_upper = id_range.split('-')
    print(id_lower, id_upper)
    for id in range(int(id_lower), int(id_upper)+1):
        if len(str(id)) % 2 == 0:
            pass