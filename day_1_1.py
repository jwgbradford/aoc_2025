with open('day_1_1_input.txt') as my_file:
    data : list[str] = my_file.read().splitlines()

password : int = 0
dial : int = 50

for line in data:
    direction : str = line[0]
    steps : int = int(line[1:])

    steps = steps % 100 # since the dial wraps around every 100

    if direction == 'R':
        dial += steps
    elif direction == 'L':
        dial -= steps

    if dial > 99:
        dial = dial - 100
    elif dial < 0:
        dial = dial + 100

    if dial == 0:
        password += 1

print(password)