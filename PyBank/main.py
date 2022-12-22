# Import dependencies
# OS helps us create a filepath across operating systems. 
# CSV is a module for reading csv files. 
import os
import csv

# Path to collect budget data from Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# CSV reader specifies delimiter and variable that holds contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header
    header = next(csvreader)

    # intialize variables
    date_list = []
    pl_list = []
    monthly_change = []
    net_total = 0
    
    past_value = 0
    past_change = 0
    greatest_decrease = 0
    greatest_increase = 0
    increase_date = 0
    decrease_date = 0
  
    # Read each row of data
    for row in csvreader:
        # Create lists for dates and profit/losses
        date_list.append(row[0])
        pl_list.append(row(1))
    
        # Find net profit and loss. 
        net_total += int(row[1])
        
        # Calculate change between first day and second day and add to list.  
        monthly_change = int(row[1]) - past_value
        #changes_list.append(change)
        
        # Get greatest increase and decrease in profit - check each row against the previous. 
        #if change > past_change:
        #    greatest_increase = change
        #    increase_date = row[0]
        #elif change < past_change:
        #    greatest_decrease = change
        #    decrease_date = row[0]
        


        # Reset past values to current row.
        past_value = int(row[1])
        past_change = change

       
    # Count number of months to get total number of months in data set. 
    #months = len(date_list)

    # Sum changes and divide by number of entries
    #average = sum(changes_list) / months
    #average = net_total / (months - 1)
    #get greatest profit
    #changes_list.sort(reverse=True)
    #greatest_increase = changes_list[0]
    #get greatest decrease in profits
    #changes_list.sort(reverse=False)
    #greatest_decrease = changes_list[0]


    #print
    print(f'Financial Analysis')
    print("-"*30)
    print(f'Total Months: {months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {increase_date} ${greatest_increase}')
    print(f'Greatest Decrease in Profits: {decrease_date}  ${greatest_decrease}')



# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


