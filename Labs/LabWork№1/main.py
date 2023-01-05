#Theory of Probability and Mathematical Statistics. LabWork №1 made by Vladyslav Lytvynchuk, group IPS-21/1
#Created: 06/10/2022
#Modified: 18/10/2022

import os
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import statistics

def getTableOfFrequencyAndCumulativeFrequency(file_name):
    frequency_set = getArrayOfFrequency(file_name)
    cumulative_frequency_set = getArrayOfCumulativeFrequency(frequency_set)
    print(frequency_set)
    print(cumulative_frequency_set)
    # columns = ('Frequency', 'Cumulative Frequency')
    # rows = range(1, data_length + 1)
    # plt.figure(facecolor='white', num='Завдання №1', figsize=(7,7), tight_layout={'pad':1})
    # ax = hideAxesAndEdgeFromPlot()
    # # Table of frequencies and cumulative frequencies
    # the_table = ax.table(cellText=data_matrix,
    #          rowLabels=rows,
    #          colLabels=columns,
    #          loc='center')
    # the_table.scale(1.1, 1.5)
    # plt.title("Таблиця частот і кумулятивних частот для переглянутих фільмів")
    # plt.show()
    # writeFrequencyToFile(data_matrix, data_length, max_freq)

def getDictOfFrequencies(file_name):
    with open(f'{file_name}', 'r') as f:
        data_length = int(f.readline())
        data_set = [[int(number) for number in line.split()][0] for line in f]

    frequency_dict = {}
    for views_count in data_set:
        if views_count in frequency_dict:
            frequency_dict[views_count] += 1
        else:
            frequency_dict[views_count] = 1
    return frequency_dict

def getDictOfCumulativeFrequencies(frequencies_dict):
    cumulative_frequency = [0] * len(frequencies_dict)
    for frequency in frequencies_dict.values():
        cumulative_frequency[index] += frequency
    return cumulative_frequency

# def getArrayOfFrequencyAndCumulativeFrequencyWithMaxFreq(file_name):
#     cumulative_frequency = 0
#     with open(f'{file_name}', 'r') as f:
#         data_length = int(f.readline())
#         data = [[int(number) for number in line.split()] for line in f]
#     max_freq = getMode(data)
#     for number in data:
#         cumulative_frequency += int(number[0])
#         number.append(cumulative_frequency)
#     return data, data_length, max_freq

def writeFrequencyToFile(data_cum_and_stan_frequencies, data_length, max_freq):
    with open('output_1.txt', 'w') as f:
        f.write(f"Number of films: {data_length}")
        f.write("\nFilm\tFrequency\tCumulative Frequency\n")
        index = 1
        for row in data_cum_and_stan_frequencies:
            f.write(f"{index}\t\t")
            for value in row:
                f.write(f"|\t{value}\t|\t\t")
            index += 1
            f.write("\n")
        for key, value in max_freq.items():
            f.write(f"The most watched film from this distribution is {key} - {value} times")

def hideAxesAndEdgeFromPlot():
    ax = plt.gca()
    # Hide axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.box(on=None)
    return ax

def getModeAndMedian(file_name):
    with open(f'{file_name}', 'r') as f:
        data_length = f.readline()
        data_frequencies = [int([number for number in line.split()][0]) for line in f]
    # Finding mode of the given dataset
    mode = getMode(data_frequencies)
    # Finding median of the given dataset
    median = getMedian(data_frequencies)
    for key, value in mode.items():
        print(f"\nElement {key} occurs {value} times, therefore {key} is mode of the data")
    print(f"Element {median} is median of given dataset\n")
    with open("output_2.txt", 'w') as f:
        f.write(f"Mode and median of given dataset\n"
                f"Number of films: {data_length}"
                f"\nElement {key} occurs {value} times, therefore {key} is mode of the data\n"
                f"Element {median} is median of given dataset\n")

def getMode(data_frequencies):
    mode = np.amax(data_frequencies)
    mode_index = data_frequencies.index(mode) + 1
    # mode_index = np.argmax(data_frequencies) + 1
    return {mode_index: mode}

def getMedian(data_frequencies):
    data_values = getDataValues(data_frequencies)
    middle_index = round(len(data_values) / 2)
    if len(data_values) % 2 != 0:
        median = data_values[middle_index]
    else:
        median = (data_values[middle_index] + data_values[middle_index + 1]) / 2
    return median
    # return statistics.median(data_values)

def getDataValues(data_frequencies):
    data_values = []
    value = 1
    for frequency in data_frequencies:
        for number_of_appearances in range(frequency):
            data_values.append(value)
        value += 1
    return data_values

# def fillArray(data:int, length:int, list, index, actual_number_of_elements):
#     list.append(index + 1)
#     actual_number_of_elements += 1
#     if len(list) == length:
#         return list
#     if actual_number_of_elements == data[index]:
#         actual_number_of_elements = 0
#         index += 1
#     return fillArray(data, length, list, index, actual_number_of_elements)

def getVarianceAndStandartDeviation(file_name):
    with open(f'{file_name}', 'r') as f:
        data_length = f.readline()
        data_frequencies = [int([number for number in line.split()][0]) for line in f]
    variance = getVariance(data_frequencies)
    standard_deviation = getStandardDeviation(getDataValues(data_frequencies))
    print(f"Number of films: {data_length}"
          f"\nVariance of given data is {variance}")
    print(f"Standard deviation of given data is {standard_deviation}\n")
    with open('output_3.txt', 'w') as f:
        f.write("Variance and Standard Deviation of given dataset"
                f"\nVariance of given data is {variance}\n"
                f"Standard deviation of given data is {standard_deviation}\n")

def getVariance(data_frequencies):
    data_values = getDataValues(data_frequencies)
    standard_deviation = getStandardDeviation(data_values)
    variance = pow(standard_deviation, 2)
    return variance

def getStandardDeviation(data_values):
    # getting average value of the data set
    mean = getMean(data_values)
    sum_of_deviations = 0
    for value in data_values:
        sum_of_deviations += pow(value - mean, 2)
    standard_deviation = pow(sum_of_deviations/(len(data_values)), 0.5)
    return standard_deviation

def getMean(data_values):
    sum_of_data = sum(data_values)
    mean = sum_of_data / len(data_values)
    return mean

def getHistogramView(file_name):
    with open(f'{file_name}', 'r') as f:
        data_length = f.readline()
        data = [int([number for number in line.split()][0]) for line in f]
    pos_list = np.arange(1, len(data) + 1)
    color_set = ('.00', '.25', '.50', '.75')
    color_list = [color_set[(len(color_set) * val) // (100 * len(data))] for val in data]
    plt.figure(facecolor='white', num='Завдання №5')
    ax = plt.axes()
    ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(pos_list))
    ax.xaxis.set_major_formatter(mpl.ticker.FixedFormatter(pos_list))
    plt.xlabel("Movie Number")
    plt.ylabel("Frequency")
    plt.bar(pos_list, data, color=color_list, width=0.5)
    plt.title("Distribution histogram")
    for position_x in pos_list:
        plt.text(position_x, data[position_x - 1] + 1, data[position_x - 1], horizontalalignment='center')
    plt.show()
    writeHistogramToFile(data)

def writeHistogramToFile(data_frequencies):
    unique_frequencies = getUniqueValue(data_frequencies)
    unique_frequencies.sort(reverse=True)
    with open("output_4.txt", 'w') as f:
        f.write("Frequency\n")
        for frequency in unique_frequencies:
            f.write(f"\t{frequency}\t")
            for film_number in range(len(data_frequencies)):
                f.write(f"\t|") \
                    if data_frequencies[film_number] >= frequency \
                    else f.write("\t")
            f.write("\n")
        f.write("\t\t")
        for film_number in range(len(data_frequencies)):
            f.write(f"\t{film_number + 1}")

def getUniqueValue(data_set):
    unique_values = []
    for value in data_set:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values


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


if __name__ == '__main__':
    _exit_ = False
    file_name = "input_10.txt"
    showMenu()
    print(f"Workable file: {file_name}")
    while not (_exit_):
        choose = int(input("Choose number of the task (from 1 to 6): "))
        match choose:
            case 1:
                print(f"\nChosen file: {file_name}\n")
                showFiles()
                file_name = chooseInputFile()
            case 2:
                getTableOfFrequencyAndCumulativeFrequency(file_name)
                print("\nInformation was writen to the output_1.txt file\n")
            case 3:
                getModeAndMedian(file_name)
                print("\nInformation was writen to the output_2.txt file\n")
            case 4:
                getVarianceAndStandartDeviation(file_name)
                print("\nInformation was writen to the output_3.txt file\n")
            case 5:
                getHistogramView(file_name)
                print("\nInformation was writen to the output_4.txt file\n")
            case _:
                _exit_ = True