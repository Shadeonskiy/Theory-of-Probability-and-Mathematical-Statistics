# Theory of Probability and Mathematical Statistics. LabWork №4 made by Vladyslav Lytvynchuk, group IPS-21/1
# Created: 22/10/2022
# Modified: 22/10/2022

import math as m

def C(k, n):
    result = m.factorial(n) / (m.factorial(k) * m.factorial(n - k))
    return result

def task_1():
    black_pair = 40
    brown_pair = 26
    red_pair = 22
    blue_pair = 12
    amount_of_pairs = black_pair + brown_pair + red_pair + blue_pair

    probability = (red_pair + blue_pair) / amount_of_pairs
    return probability


def task_2():
    N = 10  # 10 employees
    M = 8  # 8 CONSULTANTS
    n = 2  # choose 2 workers from 10
    m = 1  # at least 1 consultant
    P_inv = C(n, N - M) / C(n, N)  # Probability of 8 workers, not consultants
    P = 1 - P_inv
    return P


def task_3():
    N = 10  # 10 MANAGERS
    M = 2  # 2 relatives
    n = 3  # choose 3 managers from 10
    m = 1  # at least 1 relative
    P_inv = C(n, N - M) / C(n, N)  # Probability of 8 managers, not relatives
    P = 1 - P_inv
    return P


def task_4():
    probability_first = 0.15
    probability_second = 0.25
    probability_third = 0.2
    probability_fourth = 0.1
    probability_fifth = round(1 - (probability_first + probability_second + probability_third + probability_fourth), 1)
    return probability_fifth


def task_5():
    amount_of_trains = 80
    amount_of_railways = 120
    probability = C(2, amount_of_trains) / C(2, amount_of_railways)
    return probability


def task_6():
    standard_detail = 0.9
    detail_of_the_first_grade = 0.8

    probability_of_occurrence_of_two_independent_events = round(standard_detail * detail_of_the_first_grade, 3)
    return probability_of_occurrence_of_two_independent_events


def task_7():
    N = 10  # total number of students
    M = 20  # number of questions
    A = 3  # number of perfectly prepared students
    B = 4  # number of well prepared students
    C = 2  # number of averagely prepared students
    D = 1  # number of bad prepared students

    correct_answers_from_perfectly = A / N * \
                                     20 / M * \
                                     19 / (M - 1) * \
                                     18 / (M - 2)
    correct_answers_from_well = B / N * \
                                16 / M * \
                                15 / (M - 1) * \
                                14 / (M - 2)
    correct_answers_from_averagely = C / N * \
                                     10 / M * \
                                     9 / (M - 1) * \
                                     8 / (M - 2)
    correct_answers_from_bad = D / N * \
                               5 / M * \
                               4 / (M - 1) * \
                               3 / (M - 2)

    probability_of_correct_answer = correct_answers_from_perfectly + \
                                    correct_answers_from_well + \
                                    correct_answers_from_averagely + \
                                    correct_answers_from_bad

    probability_of_perfectly_prepared = round(correct_answers_from_perfectly / probability_of_correct_answer, 3)
    probability_of_bad_prepared = round(correct_answers_from_bad / probability_of_correct_answer, 3)
    return probability_of_perfectly_prepared, probability_of_bad_prepared

def task_8():
    first_line = 0.4
    first_line_standard_detail = 0.9
    second_line = 0.3
    second_line_standard_detail = 0.95
    third_line = 0.3
    third_line_standard_detail = 0.95

    probability_of_standard_detail = round(first_line * first_line_standard_detail + \
                                     second_line * second_line_standard_detail + \
                                     third_line * third_line_standard_detail, 3)
    return probability_of_standard_detail


def task_9():
    pneumonia_in_hospital = 0.4
    peritonit_in_hospital = 0.3
    angina_in_hospital = 0.3

    probability_of_pneumonia = 0.8
    probability_of_peritonit = 0.7
    probability_of_angina = 0.85

    probability = round((peritonit_in_hospital * probability_of_peritonit) / (
                pneumonia_in_hospital * probability_of_pneumonia + peritonit_in_hospital * probability_of_peritonit + angina_in_hospital * probability_of_angina),3)
    return probability


def task_10():
    high_qualification = 0.3
    average_qualification = 0.7

    quality_high = 0.9
    quality_average = 0.8

    probability = round((high_qualification * quality_high) /
                        (high_qualification * quality_high + average_qualification * quality_average),3)
    return probability


if __name__ == '__main__':
    print("\nLabWork №4 made by Vladyslav Lytvynchuk, group IPS-21/1. Ticket №11\n")
    print(f'Task 1. Probability of red or blue pair = {task_1()}\n')
    print(f'Task 2. Probability of randomly selected two employees, at least one will be a consultant = {task_2()}\n')
    print(f'Task 3.Probability of randomly selected three managers, at least one will be a relative = {task_3()}\n')
    print(f'Task 4. Probability of assigning the product to the fifth department = {task_4()}\n')
    print(f'Task 5. Probability of arrival of two trains on adjacent tracks = {task_5()}\n')
    print(f'Task 6. Probability of producing a product of the first grade by this machine = {task_6()}\n')
    perfectly_probability, bad_probability = task_7()
    print(f'Task 7.1. Probability of answering three questions by perfectly prepared student = {perfectly_probability}\n')
    print(f'Task 7.2. Probability of answering three questions by bad prepared student = {bad_probability}\n')
    print(f'Task 8. Probability of randomly taken detail to be standard = {task_8()}\n')
    print(f'Task 9. Probability of recovery of a patient with peritonitis = {task_9()}\n')
    print(f'Task 10. Probability of producing a high-quality device by a highly skilled worker = {task_10()}\n')
