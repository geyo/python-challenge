# python-challenge

![Benjamin Franklin](https://github.com/geyo/python-challenge/blob/main/python-challenge/Images/revenue-per-lead.png)

## PyBank

To gather all the data, I created a for loop that iterates the total months and profit/loss net totals, and created two seperate lists to track months and profits. 

These lists were used to figure out the change in profits from month to month. 

While the for loop is iterating, an if statement will check if the value in the row is greater than largest value found. Another if statement is checking for the lowest value. 

Additionally, the final monthly changes are iterated. 

The final average change is found by dividing the aggregated total monthly changes by the the total months (minus 1, to account for len). 

Finally, the file is printed to the terminal, and a new file with the message is added to the analysis folder. 

## PyPoll

First, a path to open the csv is created. 

Within a with block, the csv file is read (while making sure to skip the header.)

A for loop reads every row in the csv file and iterates the total votes. 
If a row does not contain the candidate's name in the dictionary, then the candidate is added along with a single vote. 
If a row does contain the candidate's name in the dictionary, then a value for that candidate key is iterated in the dictionary. 

Finally, each candidate's name and total votes are assigned to a list and variables, and the percentage of votes received is calculated. 

The winner is found using a max function on the candidate dictionary.

Finally the message is printed to the terminal and added to a new file in the analysis folder. 
