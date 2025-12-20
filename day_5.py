with open('day_5_input.txt') as file:
    data = file.read().split()

#print(data)

ingredients = []
available = []

for entry in data:
    if '-' in entry:
        ingredients.append(entry.split('-'))
    else:
        available.append(int(entry))

fresh = 0

for item in available:
    for test_range in ingredients:
        if int(test_range[0]) <= item <= int(test_range[1]):
            fresh += 1
            break

print(fresh)