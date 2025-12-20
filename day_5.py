def check_overlap(range1, range2) -> bool:
        return max(range1[0],range2[-1]) < min(range1[-1],range2[0])

with open('day_5_test.txt') as file:
    data = file.read().split()

#print(data)

ingredients = []
available = []

for entry in data:
    if '-' in entry:
        lower, upper = entry.split('-')
        ingredients.append([int(lower), int(upper)])
    else:
        available.append(int(entry))

print(ingredients)
range_list = []

for test_range in ingredients:
    if len(range_list) == 0:
        range_list.append(test_range)
    else:
        no_overlap = True
        for overlap in range_list:
            if max(test_range[0],overlap[0]) < min(test_range[-1],overlap[-1]):
                if overlap[0] < test_range[0]:
                    test_range[0] = overlap[0]
                if overlap[-1] > test_range[-1]:
                    test_range[-1] = overlap[-1]
                no_overlap = False
                break
        if no_overlap:
            range_list.append(test_range)

print(range_list)

range_counter = 0
for each_range in range_list:
    range_counter += each_range[1]-each_range[0] + 1

print(range_counter)
'''
fresh = 0

for item in available:
    for test_range in ingredients:
        if int(test_range[0]) <= item <= int(test_range[1]):
            fresh += 1
            break

print(fresh)
'''