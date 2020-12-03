
with open("input.txt", 'r') as file:
    LINES = file.read().splitlines()

def get_number_of_trees_encountered(number_right=3, number_down=1):
    number_of_trees = 0
    position_character = 0
    line_size = len(LINES[0])
    for line_number in range(0,len(LINES), number_down): #range(len(LINES))
        if line_number != 0:
            position_character += number_right
        if position_character > line_size-1:
            position_character = (position_character - line_size) 
        character = get_character_from_position_in_lines(line_number, position_character)
        if is_character_a_tree(character):
            number_of_trees += 1
    return number_of_trees



def get_character_from_position_in_lines(line_number, character_position):
    return LINES[line_number][character_position]

def is_character_a_tree(character):
    isTree = False
    if character == '#':
        isTree = True
    return isTree


def get_multiple_trees_with_several_slopes():
    trees_1_1 = get_number_of_trees_encountered(1 , 1)
    trees_3_1 = get_number_of_trees_encountered(3 , 1)
    trees_5_1 = get_number_of_trees_encountered(5 , 1)
    trees_7_1 = get_number_of_trees_encountered(7 , 1)
    trees_1_2 = get_number_of_trees_encountered(1 , 2)
    print(trees_1_1, trees_3_1, trees_5_1, trees_7_1, trees_1_2)
    multiple_trees = trees_1_1 * trees_3_1 * trees_5_1 * trees_7_1 * trees_1_2
    return multiple_trees



if __name__ == '__main__':
    print(get_multiple_trees_with_several_slopes())
