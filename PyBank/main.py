 # Import modules 
import os
import csv

# Define variables
month_count = 0
date_list = []
profit_l_list = []
total_p_l = float(0)
change_value_list = []
prior_value = float(0)

# Define path to budget data csv
csvpath = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')

# Open csv
with open(csvpath, 'r', newline='') as csvfile:

# Define csv_reader
    csv_reader = csv.reader(csvfile, delimiter=',')

# Identify header of the csv file and skip over it
    csv_header = next(csv_reader)

# Loop through the dataset to count months and add to list of dates and profit/loss values
    for value in csv_reader:
        month_count += 1
        date_list.append(str(value[0]))
        profit_l_list.append(float(value[1]))

    # Create list of profit/loss changes month-to-month
        current_value = value[1]
        change_value = float(current_value) - float(prior_value)
        change_value_list.append(change_value)
        prior_value = current_value
        

# Define function to calc avg change in profit/loss between months
def average(change_value_list):
    x = len(change_value_list)
    total = sum(change_value_list) - change_value_list[0]
    avg = total / (x - 1)
    return avg

# Calc avg change
average_change = round(average(change_value_list), 2)

# Calc total profit/loss 
total_p_l = round(sum(profit_l_list))

# Match dates with the highest and lowest profit/loss values
highest_p_l = round(max(profit_l_list))
lowest_p_l = round(min(profit_l_list))
highest_index = profit_l_list.index(highest_p_l)
lowest_index = profit_l_list.index(lowest_p_l)

# Display output via terminal screen   
print("------------------------------")
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_p_l}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_list[highest_index]} (${highest_p_l})")
print(f"Greatest Decrease in Profits: {date_list[lowest_index]} (${lowest_p_l})")

# Create output path
output_path = os.path.join('..', 'PyBank','Analysis',"Financial_Analysis.txt")
with open(output_path, 'w', newline='') as text_file:

# Write the report to a text file within the Output folder
    print('-----------------------------', file=text_file)
    print("Financial Analysis", file=text_file)
    print('-----------------------------', file=text_file)
    print(f"Total Months: {month_count}", file=text_file)
    print(f"Total: ${total_p_l}", file=text_file)
    print(f"Average Change: ${average_change}", file=text_file)
    print(f"Greatest Increase in Profits: {date_list[highest_index]} (${highest_p_l})", file=text_file)
    print(f"Greatest Decrease in Profits: {date_list[lowest_index]} (${lowest_p_l})",file=text_file)