from math import floor
from math import ceil


with open("input.txt", 'r') as file:
    BOARDING_PASSES = file.read().splitlines()

MIN_POSSIBLE_ROW = 0
MAX_POSSIBLE_ROW = 127
MIN_POSSIBLE_COLUMN = 0
MAX_POSSIBLE_COLUMN = 7

def get_seat_Ids():
    seat_IDs = []
    for boarding_pass in BOARDING_PASSES:
        min_possible_row = MIN_POSSIBLE_ROW
        max_possible_row = MAX_POSSIBLE_ROW
        min_possible_column = MIN_POSSIBLE_COLUMN
        max_possible_column = MAX_POSSIBLE_COLUMN
        letters_boarding_pass = list(boarding_pass)
        for index_letter in range(len(letters_boarding_pass)):
            if index_letter < 7:
                min_possible_row, max_possible_row = update_max_and_min_position(letters_boarding_pass[index_letter], min_possible_row, max_possible_row)
            else:
                min_possible_column, max_possible_column = update_max_and_min_position(letters_boarding_pass[index_letter], min_possible_column, max_possible_column)
        
        seat_Id = (max_possible_row * 8) + max_possible_column
        seat_IDs.append(seat_Id)
    return sorted(seat_IDs)


def update_max_and_min_position(letter, min_possible_position, max_possible_position):
    medium_value = (min_possible_position + max_possible_position) / 2
    if letter in ['F', 'L']:
        return min_possible_position, floor(medium_value)
    elif letter in ["B", "R"]:
        return ceil(medium_value), max_possible_position

def get_your_seat_id():
    liste = get_seat_Ids()
    for index_seat in range(1, len(liste)):
        if liste[index_seat] - liste[index_seat-1] != 1:
            your_seat = liste[index_seat]-1
            break

    return your_seat


if __name__ == '__main__':

    # Puzzle 1
    # print(max(get_seat_Ids()))
    # Puzzle 2
    print(get_your_seat_id())