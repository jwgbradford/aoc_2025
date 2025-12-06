from math import modf
with open('day_1_test.txt') as my_file:
    data : list[str] = my_file.read().splitlines()

password : int = 0
dial : int = 50

for line in data:
    direction : str = line[0]
    steps : int = int(line[1:])

    password += modf(steps / 100)[1] # add the number of full rotations to the password
    steps = steps % 100 # since the dial wraps around every 100

    if direction == 'R':
        dial += steps
    elif direction == 'L':
        dial -= steps

    # need to catch the case where we wrap around the dial, but not count if we start on 0
    if dial > 99:
        dial = dial - 100
    elif dial < 0:
        dial = dial + 100
    
    if dial == 0:
        password += 1
    print(f"Direction: {direction}, Steps: {steps}, Dial: {dial}, Current Password: {password}")

print(password)