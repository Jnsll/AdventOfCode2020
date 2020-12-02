import re

valid_passwords_puzzle1 = 0
valid_passwords_positions = 0

with open("input", 'r') as file:
    lines = file.readlines()

for line in lines:
    m = re.search(r'(\d+)-(\d+)\s(\w):\s(\w+)', line)
    if m is not None:
        min_occurence = int(m.group(1))
        max_occurence = int(m.group(2))
        letter = m.group(3)
        password = list(m.group(4))

        number_occurence = password.count(letter)
        if number_occurence >= int(min_occurence) and number_occurence <= int(max_occurence):
            valid_passwords_puzzle1 += 1


        position_first = min_occurence
        position_second = max_occurence

        letters_at_positions = [password[position_first-1], password[position_second-1]]
        occurence_at_positions = letters_at_positions.count(letter)
        if occurence_at_positions ==1:
            valid_passwords_positions += 1

print(valid_passwords_puzzle1)
print(valid_passwords_positions)
