with open('day_1_input.txt') as my_file:
    data : list[str] = my_file.read().splitlines()

password : int = 0
dial : int = 50
dial_is_zero : bool = False

for line in data:
    direction : str = line[0]
    steps : int = int(line[1:])

    password += steps // 100 # add the number of full rotations to the password
    steps = steps % 100 # since the dial wraps around every 100

    if direction == 'R':
        dial += steps
    elif direction == 'L':
        dial -= steps

    if dial > 99:
        dial = dial - 100
        if not dial_is_zero and dial != 0:
            password += 1
    elif dial < 0:
        dial = dial + 100
        if not dial_is_zero:
            password += 1

    if dial == 0:
        password += 1
        dial_is_zero = True
    else:
        dial_is_zero = False
    #print(f"Direction: {direction}, Steps: {steps}, Dial: {dial}, Current Password: {password}")

print(password)