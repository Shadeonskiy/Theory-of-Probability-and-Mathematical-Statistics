# Theory of Probability and Mathematical Statistics. LabWork №4 made by Vladyslav Lytvynchuk, group IPS-21/1
# Created: 24/10/2022
# Modified: 24/10/2022

import math
from sympy import *

def C(k, n):
    result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return result

def P(k, n, p):
    q = 1 - p
    result = C(k, n) * (p ** k) * (q ** (n - k))
    return result

def getPhiGauss(m, n, p):
    x = getX(m, n, p)
    if x > 5:
        return 0.5
    if x < -5:
        return -0.5

    expression = (pow(1, x) / math.sqrt(2 * math.pi)) * exp(-(x ** 2)/2)
    return expression

def getPhiIntegral(m, n, p):
    x = Symbol('x')
    expression = (pow(1, x) / math.sqrt(2 * math.pi)) * integrate((exp(-(x ** 2) / 2)), (x, 0, x))

    X = getX(m, n, p)
    if X > 5:
        return 0.5
    if X < -5:
        return -0.5

    return expression.evalf(subs={x: X})

def getX(m, n, p):
    q = 1 - p
    result = (m - n * p) / math.sqrt(n * p * q)
    return result

def task_1():
    probability = 0.2
    amount_of_attempts = 5
    min_amount_of_successes = 3

    probability_of_successful_operations = round(P(min_amount_of_successes, amount_of_attempts, probability), 4)
    return probability_of_successful_operations

def task_2():
    probability = 0.8
    amount_of_attempts = 5
    min_amount_of_successes = 4

    A_probability_of_successful_operations = round(P(min_amount_of_successes, amount_of_attempts, probability), 4)
    B_probability_of_successful_operations = round(P(min_amount_of_successes, amount_of_attempts, probability) + P(min_amount_of_successes + 1, amount_of_attempts, probability), 4)
    return A_probability_of_successful_operations, B_probability_of_successful_operations

def task_3():
    amount_of_candies = 400 # n
    min_amount_of_goodies = 80 # m
    probability_of_goody = 0.2 # p
    q = 1 - probability_of_goody
    phi = getPhiGauss(min_amount_of_goodies, amount_of_candies, probability_of_goody)

    # x = getX(min_amount_of_goodies, amount_of_candies, probability_of_goody)
    # if x == 0 : phi = 0.3989

    probability = phi / math.sqrt(amount_of_candies * probability_of_goody * q)
    return probability

def task_4():
    amount_of_cars = 100000
    min_amount_of_defective_cars = 5
    probability_of_defective = 0.0001

    return round(P(min_amount_of_defective_cars, amount_of_cars, probability_of_defective), 4)

def task_5():
    high_grade_probability = 0.4 # p
    amount_of_pairs = 600 # n
    m1 = 228
    m2 = 252
    phi1 = getPhiIntegral(m1, amount_of_pairs, high_grade_probability)
    phi2 = getPhiIntegral(m2, amount_of_pairs, high_grade_probability)

    # x1 = getX(m1, amount_of_pairs, high_grade_probability)
    # x2 = getX(m2, amount_of_pairs, high_grade_probability)
    #
    # if x1 == -1.0 : phi1 = -0.3413
    # if x2 == 1.0 : phi2 = 0.3413

    probability = round(phi2 - phi1 , 4)
    return probability

def task_6():
    number_of_clients = 100 # n
    financial_operation_probability = 0.4 # p

    q = 1 - financial_operation_probability
    k0 = number_of_clients * financial_operation_probability - q # np - q
    k1 = number_of_clients * financial_operation_probability + financial_operation_probability # np + p

    most_likely_number = round((k0+k1)/2)
    probability = round(P(most_likely_number, number_of_clients, financial_operation_probability), 4)
    return most_likely_number, probability

def task_7():
    non_standard_detail = 0.04
    amount_of_details = 4000
    m1 = 0
    m2 = 170
    phi1 = getPhiIntegral(m1, amount_of_details, non_standard_detail)
    phi2 = getPhiIntegral(m2, amount_of_details, non_standard_detail)

    # x1 = getX(m1, amount_of_details, non_standard_detail)
    # x2 = getX(m2, amount_of_details, non_standard_detail)
    #
    # if x1 == -12.909944487358056 : phi1 = -0.5
    # if x2 == 0.8068715304598785 : phi2 = 0.2881

    probability = round(phi2-phi1,4)
    return probability

def task_8():
    n = 10000
    m = 5000
    p = 0.5
    q = 1 - p
    phi = getPhiGauss(m, n, p)

    # x = getX(m, n, p)
    # if x == 0 : phi = 0.3989

    result = round(phi / math.sqrt(n * p * q), 6)
    return result

def task_9():
    amount_of_products = 1000
    min_amount_of_damaged = 5
    probability_of_damaged = 0.002

    return round(P(min_amount_of_damaged, amount_of_products, probability_of_damaged), 4)

def task_10():
    number_of_coins = 150
    wrong_work_probability = 0.03

    p = 1 - wrong_work_probability
    k0 = number_of_coins * p - wrong_work_probability
    k1 = number_of_coins * p + p

    most_likely_number = round((k0 + k1) / 2)
    probability = round(P(most_likely_number, number_of_coins, p), 4)
    return most_likely_number, probability

if __name__ == '__main__':
    print("\nLabWork №5 made by Vladyslav Lytvynchuk, group IPS-21/1. Ticket №11\n")
    print(f'Task 1. Probability that three out of five trains will have wagons for this destination = {task_1()}\n')
    varA, varB = task_2()
    print(f'Task 2.1. Probability that event A will occur exactly 4 times = {varA}\n')
    print(f'Task 2.2. Probability that event A will occur at least 4 times = {varB}\n')
    print(f'Task 3.Probability that 80 out of 400 candies will be goodies = {task_3()}\n')
    print(f'Task 4. Probability that 5 out of 100000 cars will be defective  = {task_4()}\n')
    print(f'Task 5. Probability that among 600 pairs of shoes from 228 to 252 pairs will be of high quality = {task_5()}\n')
    most_likely_number, probability = task_6()
    print(f'Task 6. Most likely number of financial operations from clients = {most_likely_number}, probability = {probability}\n')
    print(f'Task 7. Probability that number of non-standard details will be at least 170 out of 4000 = {task_7()}\n')
    print(f'Task 8. Probability that in 10000 independent tosses of a coin a coat of arms will fall 5000 times = {task_8()}\n')
    print(f'Task 9. Probability that 5 damaged products out of 1000 will arrive at the base = {task_9()}\n')
    most_likely_number, probability = task_10()
    print(f'Task 10. Most likely number of properly work of the machine = {most_likely_number}, probability = {probability}\n')
