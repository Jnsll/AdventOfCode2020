
import numpy as np
from collections import Counter

with open("input.txt", 'r') as file:
    data = file.read()


def resolve_puzzle1(data):
    forms = parse_input_data(data)
    number_yes_answers = get_number_of_yes_answers_for_every_groupform(forms)
    sum_yes_answers = get_sum_of_yes_answer(number_yes_answers)
    return sum_yes_answers

def resolve_puzzle2(data):
    forms = parse_input_data_2(data)
    #print(forms)
    number_of_yes_answers_by_everyone_in_a_group = get_number_of_yes_answers_for_every_groupform_2(forms)
    return get_sum_of_yes_answer(number_of_yes_answers_by_everyone_in_a_group)

def parse_input_data(input_data):
    forms = []
    answers_by_a_group = []
    for line in input_data.split('\n'):
        if not line:
            forms.append(answers_by_a_group)
            forms.append([])
            answers_by_a_group = []
        else:
            answers_by_a_person = list(line)
            answers_by_a_group.extend(answers_by_a_person)
    return forms

def parse_input_data_2(input_data):
    forms = []
    answers_by_a_group = []
    for line in input_data.split('\n'):
        if not line:
            forms.append(answers_by_a_group)
            forms.append([])
            answers_by_a_group = []
        else:
            answers_by_a_person = list(line)
            answers_by_a_group.append(answers_by_a_person)
    return forms


def get_number_of_yes_answers_for_every_groupform(forms):
    number_of_answers= []
    for group in forms:
        if group:
            number_of_answers.append(len(np.unique(group)))
    return number_of_answers

def get_number_of_yes_answers_for_every_groupform_2(forms):
    number_of_yes_answers_by_everyone = []
    for group_answers in forms:
        if group_answers:
            number_of_people_in_group = len(group_answers)
            answers_by_the_group = []
            for person_answers in group_answers:
                answers_by_the_group.extend(person_answers)
        else:
            occurences_of_answers = Counter(answers_by_the_group)
            answers_by_everyone = []
            for answer in occurences_of_answers:
                if occurences_of_answers[answer] == number_of_people_in_group:
                    answers_by_everyone.append(answer)
            number_of_yes_answers_by_everyone.append(len(answers_by_everyone))
            number_of_people_in_group = 0
    return number_of_yes_answers_by_everyone

def get_sum_of_yes_answer(number_of_yes_answers_by_group):
    return sum(number_of_yes_answers_by_group)

if __name__ == '__main__':
    #print(resolve_puzzle1(data))
    print(resolve_puzzle2(data))
