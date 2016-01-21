#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv
data = 'football.csv'
smallest_var = [100000, ""]
with open(data, 'r') as f:
	for i, row in enumerate(csv.reader(f)):
			if i == 0:
				continue
			else:
				goals = int(float(row[5]))
				goals_allowed = int(float(row[6]))
				delta = abs(goals - goals_allowed)
				arr = [delta, row[0]]
				if smallest_var[0] > arr[0]:
					smallest_var = arr
print(smallest_var)

#based on the wording, I decided we don't care about whether or not the team with the smallest difference had it in their favor,
#so I took the absolute value of the difference and sent it through a loop to find the smallest difference
#answer: 1, Aston Villa
