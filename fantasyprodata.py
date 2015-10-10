from Player import Player
import requests
# Imports data from files and creates playe classes. 
fluffcounter = 6;
qb = 15
rb = 25
te = 20 
wr = 45
flex = 60
kicker = 15
dl = 20
dst = 25

# Goes to the file and picks out the top amt of players and creates the player objets to hold them. 

# Input: Filename of data to be read, Amount of players to create, What week it is
# Output: List of Player objects
def get_position_player(url,amt):
	data = requests.get(url)
	data = data.text
	playerlist = []
	# get rid of all the stuf at the top of the page
	for x in range(0,fluffcounter):
		tmp, blank, data = data.partition("\n")
		tmp = tmp.split();
		if(tmp and tmp[0] == ("Week")):
			week = tmp[1]
	
	for x in range(0,amt):
		playerdata, blank , data = data.partition("\n")
		playerdata = playerdata.split();
		infocounter = -1
		for info in playerdata:
			if(info == "at" or info == "vs."):
				break;
			infocounter = infocounter+1
		name=""
		for y in range(1,infocounter):
			name = name + " " + playerdata[y]
		rank = playerdata[0]
		team = playerdata[infocounter]
		infocounter = infocounter+1
		matchup = playerdata[infocounter] + playerdata[infocounter+1]
		infocounter= infocounter +2 
		best = playerdata[infocounter]
		infocounter = infocounter+1
		worst = playerdata[infocounter]
		infocounter = infocounter+1
		avg = playerdata[infocounter]
		infocounter = infocounter+1
		std = playerdata[infocounter]
		newplayer = Player(name,rank,team,matchup,best,worst,avg,std,week)
		playerlist.append(newplayer)

	return playerlist
#  Offline version
# from Player import Player
# # Imports data from files and creates playe classes. 
# fluffcounter = 6;
# qb = 15
# rb = 25
# te = 20 
# wr = 45
# flex = 60
# kicker = 15
# dl = 20
# dst = 25

# # Goes to the file and picks out the top amt of players and creates the player objets to hold them. 

# # Input: Filename of data to be read, Amount of players to create, What week it is
# # Output: List of Player objects
# def get_position_player(filename,amt,week):
# 	data = open(filename,'r')
# 	playerlist = []
# 	# get rid of all the stuf at the top of the page
# 	for x in range(0,fluffcounter):
# 		data.readline();
	
# 	for x in range(0,amt):
# 		playerdata = data.readline();
# 		playerdata = playerdata.split();
# 		infocounter = -1
	# 	for info in playerdata:
	# 		if(info == "at" or info == "vs."):
	# 			break;
	# 		infocounter = infocounter+1
	# 	name=""
	# 	for y in range(1,infocounter):
	# 		name = name + " " + playerdata[y]
	# 	rank = playerdata[0]
	# 	team = playerdata[infocounter]
	# 	infocounter = infocounter+1
	# 	matchup = playerdata[infocounter] + playerdata[infocounter+1]
	# 	infocounter= infocounter +2 
	# 	best = playerdata[infocounter]
	# 	infocounter = infocounter+1
	# 	worst = playerdata[infocounter]
	# 	infocounter = infocounter+1
	# 	avg = playerdata[infocounter]
	# 	infocounter = infocounter+1
	# 	std = playerdata[infocounter]
	# 	newplayer = Player(name,rank,team,matchup,best,worst,avg,std,week)
	# 	playerlist.append(newplayer)

	# return playerlist