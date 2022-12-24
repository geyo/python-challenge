# Import dependencies
# OS helps us create a filepath across operating systems. 
# CSV is a module for reading csv files. 
import os
import csv

# Path to collect budget data from Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Establish lists
month_list = [] #list of all months
profit_loss_list = [] #list of all profits and losses

total_months = 0 #sum of all months
total_net = 0 #sum of all profit/loss 

month_to_month_pl_change = 0
current_month_pl = 0
past_month_pl= 0
current_month = 0
total_monthly_changes = 0
average = 0

most_increase = 0
most_decrease = 0
most_increase_date = 0
most_decrease_date = 0

# CSV reader specifies delimiter and variable that holds contents
# Since budget_data.csv has just two columns, it is a good candidate to apply dictreader. 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    header = next(csvreader)
    # Read each row of data
    for row in csvreader:
        # Count total months and sum total row.
        total_months += 1
        total_net += int(row[1])
        # Add to months list and pl list
        month_list.append(row[0])
        profit_loss_list.append(row[1])

        #determine current month, previous month, and current date
        #find the last pl in list and place in integer format. 
        #note--always do "len - 1" considering that indexes start at 0 
        current_month_pl = int(profit_loss_list[len(profit_loss_list) - 1]) 
        #find the second to last pl in list (aka the past month)
        #and place into integer format
        past_month_pl = int(profit_loss_list[len(profit_loss_list) - 2])
        #calculate month to month change 
        month_to_month_pl_change = current_month_pl - past_month_pl
        #capture latest month added to month list.
        current_month = month_list[len(profit_loss_list) - 1]
        
        #get greatest increase and greatest decrease
        if month_to_month_pl_change > most_increase:
            most_increase = month_to_month_pl_change
            most_increase_date = current_month
        if month_to_month_pl_change < most_decrease:
            most_decrease = month_to_month_pl_change
            most_decrease_date = current_month


        #calculate total monthly changes
        total_monthly_changes += month_to_month_pl_change


# Find average change. 
average = total_monthly_changes / (total_months - 1)

# print 
msg = f"""
Financial Analysis
-----------------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(average, 2)}
Greatest Increase in Profits: {most_increase_date} (${most_increase})
Greatest Decrease in Profits:  {most_decrease_date} (${most_decrease})
"""
print(msg)

#export results to terminal
f = open("Analysis/results.txt","w")
f.write(msg)
