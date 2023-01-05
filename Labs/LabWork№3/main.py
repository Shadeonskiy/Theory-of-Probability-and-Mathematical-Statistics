#Theory of Probability and Mathematical Statistics. LabWork №3 made by Vladyslav Lytvynchuk, group IPS-21/1
#Created: 20/10/2022
#Modified: 21/10/2022
import math
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import statistics
mpl.use('TkAgg')

def getScatterPlot(data_matrix, data_length):
    purchases_amount, times_spent = distributeMatrix(data_matrix)
    regression_line_equation, b1, b0 = getLinearRegression(data_matrix, data_length)
    y = [b1 * purchase_amount + b0 for purchase_amount in purchases_amount]

    plt.figure(facecolor='white', num='Діаграма розсіювання для даних з файлу')
    plt.title('Відношення суми покупки до часу, витраченого на покупку')
    if b1 > 0:
        plt.text(2, 70, 'Positive trend', horizontalalignment='center')
    else:
        plt.text(2, 70, 'Negative trend', horizontalalignment='center')
    plt.scatter(purchases_amount, times_spent)
    plt.plot(purchases_amount, y, "r--", label=f'Trend\n{regression_line_equation}')
    plt.legend(loc='upper left')
    plt.show()

def distributeMatrix(data_matrix):
    data_matrix.sort()
    purchases_amount = [float(data_set[:][0]) for data_set in data_matrix]
    times_spent = [int(data_set[:][1]) for data_set in data_matrix]
    return purchases_amount, times_spent

def getCenterOfWeight(data_matrix, data_length):
    purchases_amount, times_spent = distributeMatrix(data_matrix)

    meanX = round(getMean(purchases_amount, data_length), 2)
    meanY = round(getMean(times_spent, data_length), 2)

    center_of_weight = f'G({meanX}, {meanY})'
    return center_of_weight

def getCovariance(data_matrix, data_length):
    purchases_amount, times_spent = distributeMatrix(data_matrix)

    purchases_amount_mean = getMean(purchases_amount, data_length)
    times_mean = getMean(times_spent, data_length)

    sum_of_products_of_deviations = 0
    for index_of_data in range(data_length):
        purchase_deviation = purchases_amount[index_of_data] - purchases_amount_mean
        time_deviation = times_spent[index_of_data] - times_mean
        sum_of_products_of_deviations += purchase_deviation * time_deviation

    covariance = round(sum_of_products_of_deviations / (data_length), 2)
    return covariance



def getLinearRegression(data_matrix, data_length):
    purchases_amount, times_spent = distributeMatrix(data_matrix)

    covariance = getCovariance(data_matrix, data_length)
    variance = getVariance(purchases_amount)

    b1 = covariance / variance
    b0 = getMean(times_spent, data_length) - b1 * getMean(purchases_amount, data_length)

    regression_line_equation = f'y = {b1}x {"+" if b0 > 0 else "-"} {abs(b0)}'
    return regression_line_equation, b1, b0

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

def getCorrelationCoefficient(data_matrix, data_length):
    purchases_amount, times_spent = distributeMatrix(data_matrix)

    covariance = getCovariance(data_matrix, data_length)
    X_standard_deviation = getStandardDeviation(purchases_amount, data_length)
    Y_standard_deviation = getStandardDeviation(times_spent, data_length)

    correlation_coefficient = covariance / (X_standard_deviation * Y_standard_deviation)
    return correlation_coefficient

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
        data_matrix = [[number for number in line.split()] for line in file_object]
    return data_matrix, data_length

def showMenu():
    print("LabWork №3 made by Vladyslav Lytvynchuk, group IPS-21/1. Ticket №11\n\n"
          "1. Choose new file\n"
          "2. Task 1. Get Scatter Plot\n"
          "3. Task 2. Get Center of Weight and Covariance\n"
          "4. Task 3. Get Regression Line Equation y(x)\n"
          "5. Task 4. Get Correlation Coefficient\n")

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
    append_new_line('output.txt', f"Workable file: {file_name}")
    return file_name

if __name__ == '__main__':
    _exit_ = False
    file_name = "input_10.txt"
    showMenu()
    print(f"Workable file: {file_name}")
    append_new_line('output.txt', f"Workable file: {file_name}")
    while not (_exit_):
        data_matrix, data_length = readFile(file_name)
        choose = int(input("Choose number of the task (from 1 to 6): "))
        match choose:
            case 1:
                print(f"\nChosen file: {file_name}\n")
                showFiles()
                file_name = chooseInputFile()
                print(f"Workable file: {file_name}")
            case 2:
                getScatterPlot(data_matrix, data_length)
            case 3:
                center_of_weight = getCenterOfWeight(data_matrix, data_length)
                print(f'\nCenter of gravity = G(meanX, meanY) = {center_of_weight}')
                append_new_line('output.txt', f'Center of gravity = {center_of_weight}')

                covariance = getCovariance(data_matrix, data_length)
                print(f'Covariance = {covariance}')
                append_new_line('output.txt', f'Covariance = {covariance}')

                print("\nInformation was writen to the output.txt file\n")
            case 4:
                regression_line_equation = getLinearRegression(data_matrix, data_length)
                print(f'\nRegression line equation: {regression_line_equation[0]}')
                append_new_line('output.txt', f'Regression line equation: {regression_line_equation[0]}')
                print("\nInformation was writen to the output.txt file\n")
            case 5:
                correlation_coefficient = getCorrelationCoefficient(data_matrix, data_length)
                print(f'\nCorrelation coefficient = {correlation_coefficient}')
                append_new_line('output.txt', f'Correlation coefficient = {correlation_coefficient}')
                print("\nInformation was writen to the output.txt file\n")
            case _:
                _exit_ = True