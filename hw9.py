#JLouzada
#This program reads in a file and prints out the information organized by the specific data 

#Takes in the ball park data of the file and returns if it is home or away
def home_away(ballpark):
	if ballpark == "Fenway Park":
		return "Home"
	else: 
		return "Away"

#Takes in both opponent score and home team score and determines if the home team lost or won
def win_loss(home_score, opponent_score):
	if home_score > opponent_score:
		return "Win"
	else: 
		return "Loss"

#Reads file and perform calculation to determine which line of the file it is to store the correct information
#Print informtion correctly
file = open("201107_sox_games_2.txt",'r')
count = 0
for line in file:
	count = count + 1
	if count % 6 == 1:
		date = line.strip()
		#print(date)
	elif count % 6 == 2: 
		home_team = line.strip()
		#print(home_team)
	elif count % 6 == 3: 
		home_score = int(line.strip())
		#print(home_score)
	elif count % 6 == 4: 
		opponent = line.strip()
		#print(opponent)
	elif count % 6 == 5:
		opponent_score = int(line.strip())
		#print(opponent_score)
	else: 
		ballpark = line.strip()
		print(date," ", home_team," ", home_away(ballpark)," ", opponent, " ", win_loss(home_score, opponent_score)," ",opponent_score,"-", home_score)
file.close()