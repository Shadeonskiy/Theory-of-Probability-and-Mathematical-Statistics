#Theory of Probability and Mathematical Statistics. LabWork №2 made by Vladyslav Lytvynchuk, group IPS-21/1
#Created: 16/10/2022
#Modified: 19/10/2022
import math
import os
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import statistics

#def getKthQuartile(data_set, data_length, k):
 #   quartile_number = 'lower' if k == 1 else 'upper'

#    kth_quartile_index = k/4 * (data_length + 1)
 #   distance_between_values = kth_quartile_index % 1
  #  print(f"\nIndex of {quartile_number} quartile is {kth_quartile_index}")
   # append_new_line('output.txt', f"\nIndex of {quartile_number} quartile is {kth_quartile_index}")

    #after_kth_quartile_element_index = int(np.ceil(kth_quartile_index)) - 1
    #kth_quartile_index = int(kth_quartile_index) - 1

    #kth_quartile = data_set[kth_quartile_index] + distance_between_values * \
     #                (data_set[after_kth_quartile_element_index] - data_set[kth_quartile_index])
    #print(f"Value of {quartile_number} quartile is {kth_quartile}")
    #append_new_line('output.txt', f"Value of {quartile_number} quartile is {kth_quartile}")

    #return kth_quartile

def getKthPercentile(data_set, data_length, k):
    kth_percentile_index = k / 100 * (data_length + 1)
    distance_between_values = kth_percentile_index % 1
    print(f"\nIndex of {k}th percentile is {kth_percentile_index}")
    append_new_line('output.txt', f"\nIndex of {k}th percentile is {kth_percentile_index}")

    after_kth_percentile_element_index = int(np.ceil(kth_percentile_index)) - 1
    kth_percentile_index = int(kth_percentile_index) - 1

    kth_percentile = data_set[kth_percentile_index] + distance_between_values * \
                   (data_set[after_kth_percentile_element_index] - data_set[kth_percentile_index])
    print(f"Value of {k}th percentile is {kth_percentile}")
    append_new_line('output.txt', f"Value of {k}th percentile is {kth_percentile}")
    return kth_percentile

def getMeanAbsoluteDeviation(data_set, data_length):
    mean = getMean(data_set, data_length)
    sum_of_deviations = 0
    for value in data_set:
        sum_of_deviations += abs(value - mean)

    MAD = sum_of_deviations / (data_length)

    print(f"\nMean Absolute Deviation (MAD) of given data is {MAD}")
    append_new_line('output.txt', f"\nMean Absolute Deviation (MAD) of given data is {MAD}\n")
    return MAD

def getStandardDeviation(data_set, data_length):
    mean = getMean(data_set, data_length)
    sum_of_deviations = 0
    for value in data_set:
        sum_of_deviations += pow(value - mean, 2)

    standard_deviation = pow(sum_of_deviations/(data_length), 0.5)

    print(f"\nStandard deviation of given data is {standard_deviation}")
    append_new_line('output.txt', f"\nStandard deviation of given data is {standard_deviation}")
    return standard_deviation

def getMean(data_values, data_length):
    sum_of_data = sum(data_values)
    mean = sum_of_data / data_length
    return mean

def getLinearTransformation(data_values, data_length):
    a = sp.Symbol('a')
    b = sp.Symbol('b')
    mean = getMean(data_values, data_length)

    first_equation = 100 * a + b - 100
    second_equation = mean * a + b - 95

    expression_for_b = sp.sympify(sp.solve(first_equation, b)[0])
    expression_for_a = second_equation.evalf(subs={b:expression_for_b})

    value_of_a_coefficient = sp.sympify(sp.solve(expression_for_a, a)[0])
    value_of_b_coefficient = expression_for_b.evalf(subs={a:value_of_a_coefficient})

    print(f'Initial array of marks:\n{data_values}\n')
    append_new_line('output.txt', f'Initial array of marks:\n{data_values}\n')
    data_values = [mark * value_of_a_coefficient + value_of_b_coefficient for mark in data_values]
    print(f'Array of marks after linear transformation:\n{data_values}')
    append_new_line('output.txt', f'Array of marks after linear transformation:\n{data_values}\n')
    return data_values

def showStemAndLeafPlot(data_values, data_length):
    stem_min = int(min(data_values) / 10)
    stem_max = int(max(data_values) /10)

    interval = len(str(stem_min))
    stem_multiplier = 10 ** (interval)

    out = []
    out.append('Stem | Leaf\n')
    for stem in range(stem_min, stem_max + 1):
        out.append(f'{stem:4} | ')
        for value in data_values:
            if value < 10 * stem:
                continue
            if value >= 10 * (stem + 1):
                break
            out.append(f'{value % 10:1} ')
        out.append('\n')
    out.append(f'Stem multiplier: {stem_multiplier}\n')
    out.append(f'Key: X|Y => {stem_multiplier} * X + Y\n')

    print(''.join(out))
    append_new_line('output.txt', ''.join(out))

def showBoxPlot(data_values, data_length):
    min_value = min(data_values)
    max_value = max(data_values)
    first_quartile = getKthPercentile(data_values, data_length, 25)
    third_quartile = getKthPercentile(data_values, data_length, 75)
    median = getKthPercentile(data_values, data_length, 50)

    plt.figure(facecolor='white', num='Коробковий графік розподілу оцінок')
    plt.title('Оцінки студентів з предмету ЙОПІ')

    plt.text(min_value, 1.1, min_value, horizontalalignment='center')
    plt.text(max_value, 1.1, max_value, horizontalalignment='center')
    plt.text(first_quartile, 1.1, f'Q1 = {first_quartile}', horizontalalignment='center')
    plt.text(third_quartile, 1.1, f'Q3 = {third_quartile}', horizontalalignment='center')
    plt.text(median, 0.85, f'median = {median}', horizontalalignment='center')

    plt.boxplot(data_values, vert=False, autorange=True)
    plt.show()

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

def readFile(file_name):
    with open(file_name, 'r') as file_object:
        data_length = int(file_object.readline())
        data_set = [int([number for number in line.split()][0]) for line in file_object]
    return data_set, data_length

def showMenu():
    print("LabWork №2 made by Vladyslav Lytvynchuk, group IPS-21/1. Ticket №11\n\n"
          "1. Choose new file\n"
          "2. Task 1. Get Lower and Upper Quartile, 90th Percentile\n"
          "3. Task 2. Get Mean Absolute Deviation and Standard Deviation\n"
          "4. Task 3. Get Linear Transformation\n"
          "5. Task 4. Get Stem and Leaf plot\n"
          "6. Task 5. Get Box plot\n")

def showFiles():
    folder_path = 'F:\\KNU\\TPMS\\Labs\\LabWork№2\\'
    print(f"Choosing txt input file from the path {folder_path}\n")
    print(f"Choose one from the list below")
    i = 1
    for data_file in sorted(os.listdir(folder_path)):
        if ("input" in data_file.split('.')[0] and data_file.split('.')[1] == 'txt'):
            print(f"{i}) {data_file}")
            i += 1

def chooseInputFile():
    file_name = ""
    _exit_match = False
    while not (_exit_match):
        _exit_input = False
        while not(_exit_input):
            try:
                file_number = int(input("File number = "))
                _exit_input = True
            except:
                print("You've made a mistake. Try again. . .")

            match file_number:
                case 1:
                    file_name = "input_10.txt"
                    _exit_match = True
                case 2:
                    file_name = "input_100.txt"
                    _exit_match = True
                case _:
                    print("No such file exists")
    print(f"\nFile {file_name} was successfully selected\n")
    append_new_line('output.txt', f"\nWorkable file: {file_name}")
    return file_name

def MergeSort(array, array_size):
    if len(array) <= 1:
        return
    left_part_size = int(array_size / 2)
    right_part_size = array_size - left_part_size
    left_array = []
    for i in range(0, left_part_size):
        left_array.append(array[i])
    right_array = []
    for j in range(left_part_size, array_size):
        right_array.append(array[j])
    MergeSort(left_array, left_part_size)
    MergeSort(right_array, right_part_size)
    Merge(array, left_array, right_array)

def Merge(merged_array, left_part, right_part):
        left_index = 0
        right_index = 0
        target_index = 0
        size = len(left_part) + len(right_part)
        while size > 0:
            if left_index >= len(left_part):
                merged_array[target_index] = right_part[right_index]
                right_index += 1
            elif right_index >= len(right_part):
                merged_array[target_index] = left_part[left_index]
                left_index += 1
            elif left_part[left_index] <= right_part[right_index]:
                merged_array[target_index] = left_part[left_index]
                left_index += 1
            else:
                merged_array[target_index] = right_part[right_index]
                right_index += 1
            target_index += 1
            size -= 1

if __name__ == '__main__':
    _exit_ = False
    file_name = "input_10.txt"
    showMenu()
    print(f"\nWorkable file: {file_name}")
    append_new_line('output.txt', f"Workable file: {file_name}")
    while not (_exit_):
        data_set, data_length = readFile(file_name)
        MergeSort(data_set, data_length)
        choose = int(input("Choose number of the task (from 1 to 6): "))
        match choose:
            case 1:
                print(f"\nChosen file: {file_name}\n")
                showFiles()
                file_name = chooseInputFile()
            case 2:
                getKthPercentile(data_set, data_length, 25)
                getKthPercentile(data_set, data_length, 75)
                getKthPercentile(data_set, data_length, 90)
                print("\nInformation was writen to the output.txt file\n")
            case 3:
                getStandardDeviation(data_set, data_length)
                getMeanAbsoluteDeviation(data_set, data_length)
                print("\nInformation was writen to the output.txt file\n")
            case 4:
                getLinearTransformation(data_set, data_length)
                print("\nInformation was writen to the output.txt file\n")
            case 5:
                showStemAndLeafPlot(data_set, data_length)
                print("\nInformation was writen to the output.txt file\n")
            case 6:
                showBoxPlot(data_set, data_length)
            case _:
                _exit_ = True