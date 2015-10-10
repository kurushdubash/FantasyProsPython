from Player import Player
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
def get_position_player(filename,amt,week):
	data = open(filename,'r')
	playerlist = []
	# get rid of all the stuf at the top of the page
	for x in range(0,fluffcounter):
		data.readline();
	
	for x in range(0,amt):
		playerdata = data.readline();
		playerdata = playerdata.split();
		rank = playerdata[0]
		name = playerdata[1] + " " + playerdata[2]
		team = playerdata[3]
		matchup = playerdata[4] + playerdata[5]
		best = playerdata[6]
		worst = playerdata[7]
		avg = playerdata[8]
		std = playerdata[9]
		newplayer = Player(name,rank,team,matchup,best,worst,avg,std,week)
		playerlist.append(newplayer)

