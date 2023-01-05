#Theory of Probability and Mathematical Statistics. LabWork №1 made by Vladyslav Lytvynchuk, group IPS-21/1
#Created: 06/10/2022
#Modified: 18/10/2022

import os
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import statistics

def getTableOfFrequencyAndCumulativeFrequencyWithMaxFreq(data_set, data_length):
    frequency_dict = getDictOfFrequencies(data_set)
    print(frequency_dict)
    cumulative_frequency_dict = getDictOfCumulativeFrequencies(data_set)
    mode = getMode(data_set)
    with open('output_1.txt', 'w') as f:
        f.write(f"Number of films: {data_length}")
        f.write("\n Film |\t Frequency\t| Cumulative Frequency\n")
        for film_number in frequency_dict:
            f.write(f"{film_number:5} | {frequency_dict[film_number]:-5}\t\t| {cumulative_frequency_dict[film_number]:-6}\n")
        if type(mode) is dict:
            for key, value in mode.items():
                f.write(f"The most watched film from this distribution is {key} - {value} times")
        else:
            f.write(mode)

def getDictOfFrequencies(data_set):
    frequency_dict = {}
    for film_number in data_set:
        if film_number in frequency_dict:
            frequency_dict[film_number] += 1
        else:
            frequency_dict[film_number] = 1
    return frequency_dict

def getDictOfCumulativeFrequencies(data_set):
    frequency_dict = getDictOfFrequencies(data_set)
    cumulative_frequency_dict = {}
    previous_cum_freq = 0
    for film_number, frequency in frequency_dict.items():
        cumulative_frequency_dict[film_number] = frequency + previous_cum_freq
        previous_cum_freq = cumulative_frequency_dict[film_number]
    return cumulative_frequency_dict

def getModeAndMedian(data_set, data_length):
    # Finding mode of the given dataset
    mode= getMode(data_set)
    # Finding median of the given dataset
    median = getMedian(data_set, data_length)
    with open("output_2.txt", 'w') as f:
        f.write(f"\nMode and median of given dataset\n"
                f"\nNumber of films: {data_length}\n")
        print(f"\nMode and median of given dataset\n"
                f"\nNumber of films: {data_length}\n")
        if type(mode) is dict:
            for key, value in mode.items():
                f.write(f"Element {key} occurs {value} times, therefore {key} is mode of the data\n")
                print(f"Element {key} occurs {value} times, therefore {key} is mode of the data")
        else:
            f.write(mode)
            print(mode)
        f.write(f"Element {median} is median of given dataset\n")
        print(f"Element {median} is median of given dataset\n")

def getMode(data_set):
    frequency_dict = getDictOfFrequencies(data_set)
    max_frequency = 0
    modes = {}
    for film_number, frequency in frequency_dict.items():
        if frequency > max_frequency:
            modes = {}
            max_frequency = frequency
            modes[film_number] = max_frequency
        elif frequency == max_frequency:
            modes[film_number] = max_frequency

    if max_frequency == 1:
        mode = 'There is no mode in current distribution'
    else:
        mode = modes
    # mode = max(frequency_dict, key=frequency_dict.get)
    return mode

def getMedian(data_set, data_length):
    middle_index = round(data_length / 2) - 1
    if data_length % 2 != 0:
        median = data_set[middle_index]
    else:
        median = (data_set[middle_index] + data_set[middle_index + 1]) / 2
    return median

def getVarianceAndStandartDeviation(data_set, data_length):
    variance = getVariance(data_set)
    standard_deviation = getStandardDeviation(data_set, data_length)
    print(f"Number of films: {data_length}"
          f"\nVariance of given data is {variance}")
    print(f"Standard deviation of given data is {standard_deviation}\n")
    with open('output_3.txt', 'w') as f:
        f.write("Variance and Standard Deviation of given dataset"
                f"\nVariance of given data is {variance}\n"
                f"Standard deviation of given data is {standard_deviation}\n")

def getVariance(data_set):
    standard_deviation = getStandardDeviation(data_set, data_length)
    variance = pow(standard_deviation, 2)
    return variance

def getStandardDeviation(data_set, data_length):
    # getting average value of the data set
    mean = getMean(data_set, data_length)
    sum_of_deviations = 0
    for value in data_set:
        sum_of_deviations += pow(value - mean, 2)
    standard_deviation = pow(sum_of_deviations/data_length, 0.5)
    return standard_deviation

def getMean(data_set, data_length):
    sum_of_data = sum(data_set)
    mean = sum_of_data / data_length
    return mean

def getHistogramView(data_set, data_length):
    frequencies_dict = getDictOfFrequencies(data_set)
    color_set = ('.00', '.25', '.50', '.75')
    color_list = [color_set[(len(color_set) * val) // max(frequencies_dict)] for val in frequencies_dict.values()]
    plt.figure(facecolor='white', num='Завдання №5')
    ax = plt.axes()
    ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(range(len(frequencies_dict))))
    ax.xaxis.set_major_formatter(mpl.ticker.FixedFormatter(list(frequencies_dict.keys())))

    plt.xlabel("Movie Number")
    plt.ylabel("Frequency")

    plt.bar(range(len(frequencies_dict)),frequencies_dict.values(), color=color_list, width=0.75)

    plt.title("Distribution histogram")
    plt.show()
    writeHistogramToFile(frequencies_dict)

def writeHistogramToFile(frequencies_dict):
    unique_frequencies = getUniqueValue(list(frequencies_dict.values()))
    unique_frequencies.sort(reverse=True)
    with open("output_4.txt", 'w') as f:
        f.write("Frequency\n")
        for frequency in unique_frequencies:
            f.write(f"\t{frequency}\t")
            for current_frequency in frequencies_dict.values():
                f.write(f"\t|") \
                    if current_frequency >= frequency \
                    else f.write("\t")
            f.write("\n")
        f.write("\t\t")
        for film_number in frequencies_dict.keys():
            f.write(f"\t{film_number}")

def getUniqueValue(data_set):
    unique_values = []
    for value in data_set:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

def readFile(file_name):
    with open(file_name, 'r') as f:
        data_length = int(f.readline())
        data_set = [int([number for number in line.split()][0]) for line in f]
    return data_set, data_length

def showMenu():
    print("LabWork №1 made by Vladyslav Lytvynchuk, group IPS-21/1. Ticket №11\n\n"
          "1. Choose new file\n"
          "2. Task 1. Get Table Of Frequency And Cumulative Frequency\n"
          "3. Task 2. Get Mode And Median of current distribution\n"
          "4. Task 3. Get Variance and Standard Deviation\n"
          "5. Task 4. Get Histogram of given distribution\n")

def showFiles():
    folder_path = 'F:\\KNU\\TPMS\\Labs\\LabWork№1\\'
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
                case 3:
                    file_name = "input_1000.txt"
                    _exit_match = True
                case _:
                    print("No such file exists")
    print(f"\nFile {file_name} was successfully selected\n")
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
    print(f"Workable file: {file_name}")
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
                getTableOfFrequencyAndCumulativeFrequencyWithMaxFreq(data_set, data_length)
                print("\nInformation was writen to the output_1.txt file\n")
            case 3:
                getModeAndMedian(data_set, data_length)
                print("\nInformation was writen to the output_2.txt file\n")
            case 4:
                getVarianceAndStandartDeviation(data_set, data_length)
                print("\nInformation was writen to the output_3.txt file\n")
            case 5:
                getHistogramView(data_set, data_length)
                print("\nInformation was writen to the output_4.txt file\n")
            case _:
                _exit_ = True