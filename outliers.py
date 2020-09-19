import numpy as np
import pandas as pd

# Find the outlier number 

times = int(input("How many numbers do you have in your list: "))
num_list = []

# Asks for the number, adds to the list
for i in range(times):
    append = float(input("Please enter the " + str(i+1) + ". number in your list: "))
    num_list.append(append)
    print("Your list of numbers now include: " + str(num_list))

# Finding 25th and 75th quantiles and the IQR
def ascend(name_of_the_list):
    name_of_the_list = name_of_the_list.sort()
    return name_of_the_list
        
ascend(num_list)
q1 = np.quantile(num_list, .25)
q3 = np.quantile(num_list, .75)
iqr = q3 - q1

# Finding the outliers
outlier_range_lower = q1 - 1.5 * iqr
outlier_range_upper = q3 + 1.5 * iqr

outliers = []
for i in range(times):
    if num_list[i] < outlier_range_lower or num_list[i] > outlier_range_upper:
        outliers.append(num_list[i])
        
    #else:
    #    print(str(i) + " is not an outlier.")

# Printing out the outliers.
for i in range(len(outliers)):
    if len(outliers) > 1:
        print(str(outliers[i]) + " are the outliers).")
    elif len(outliers) > 0:
        print(str(outliers[i]) + " is the outlier.")
    else:
        print("There were no outliers to be found.")
   
