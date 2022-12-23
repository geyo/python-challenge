# Import dependencies
# OS helps us create a filepath across operating systems. 
# CSV is a module for reading csv files. 
import os
import csv

# Path to collect budget data from Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# define parameters to use. 
date_list = []
pl_list = []
monthly_revenue_list = []

net_total = 0
total_months = 0
    
past_day_pl = 0
monthly_revenue = 0
average = 0

#greatest_decrease = 0
#greatest_increase = 0
#increase_date = 0
#decrease_date = 0


# CSV reader specifies delimiter and variable that holds contents
# Since budget_data.csv has just two columns, it is a good candidate to apply dictreader. 
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Dictreader automatically understands what is a header so no need for the skip header. 
    # Read each row of data
    for row in csvreader:

        # Find the net months and net profit/loss. 
        net_total += int(row["Profit/Losses"])
        total_months += 1

        # Add lists for dates and profit/losses
        date_list.append(row["Date"])
        pl_list.append(row["Profit/Losses"])

        # Calculate monthly revenue by subtracting current day from past day
        # Updaate the past day value. 
        # Add monthly revenue to list.  
        monthly_revenue = int(row["Profit/Losses"]) - past_day_pl
        past_day_pl = int(row["Profit/Losses"])
        monthly_revenue_list.append(monthly_revenue)
        #average = sum(monthly_revenue_list) / total_months


        # Get greatest increase and decrease in profit - check each row against the previous. 
        #current_month = pl_list[]
                
        #if change > past_change:
        #     = change
        #    increase_date = row[0]
        #elif change < past_change:
        #    greatest_decrease = change
        #    decrease_date = row[0]
        


        # Reset parameters for past date/revenue. 

        #past_change = change

    # Calculate average by summing monthly revenue list and dividing by number of months. 
    average = sum(monthly_revenue_list) / total_months

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
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: increase_date $greatest_increase')
    print(f'Greatest Decrease in Profits: decrease_date  $greatest_decrease')



# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


