from Player import Player
import requests
import os
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
def get_position_player(filename,amt):
	data = open(filename,'r')
	playerlist = []
	for x in range(0,fluffcounter):
		playerdata = data.readline();
		playerdata = playerdata.split();
		if(playerdata and playerdata[0] == ("Week")):
			week = playerdata[1]
	
	for x in range(0,amt):
		playerdata = data.readline()
		playerdata = playerdata.split();
		infocounter = -1
		for info in playerdata:
			if(info == "at" or info == "vs."):
				break;
			infocounter = infocounter+1
		name=""
		for y in range(1,infocounter):
			name = name + " " + playerdata[y]
		rank = int(playerdata[0])
		team = playerdata[infocounter]
		infocounter = infocounter+1
		matchup = playerdata[infocounter] + playerdata[infocounter+1]
		infocounter= infocounter +2 
		best = int(playerdata[infocounter])
		infocounter = infocounter+1
		worst = int(playerdata[infocounter])
		infocounter = infocounter+1
		avg = float(playerdata[infocounter])
		infocounter = infocounter+1
		std = float(playerdata[infocounter])
		newplayer = Player(name,rank,team,matchup,best,worst,avg,std,week)
		playerlist.append(newplayer)
	return playerlist


# @param dl: desired position acronym
# @return: player_object list for that position
def get_all_players(inputstr):
	object_list = []
	if inputstr == "dl":
		object_list = get_position_player("data/" + inputstr, dl)
	elif inputstr == "qb":
		object_list = get_position_player("data/" + inputstr, qb)
	elif inputstr == "rb":
		object_list = get_position_player("data/" + inputstr, rb)
	elif inputstr == "te":
		object_list = get_position_player("data/" + inputstr, te)
	elif inputstr == "flex":
		object_list = get_position_player("data/" + inputstr, flex)
	elif inputstr == "wr":
		object_list = get_position_player("data/" + inputstr, wr)
	elif inputstr == "kicker":
		object_list = get_position_player("data/k", kicker)
	elif inputstr == "dst":
		object_list = get_position_player("data/" + inputstr, dst)	
	elif inputstr == "ppr-flex":
		object_list = get_position_player("data/" + inputstr, flex)
	elif inputstr == "ppr-rb":
		object_list = get_position_player("data/" + inputstr, rb)
	elif inputstr == "ppr-te":
		object_list = get_position_player("data/" + inputstr, te)
	elif inputstr == "ppr-wr":
		object_list = get_position_player("data/" + inputstr, wr)
	return translate_position(tiers(object_list))


# @param pos_list: from get_all_players
# player_tuple contains: player,avg, std (tier)
# @return: list of tuples in order
def translate_position(pos_list):
	result = []
	player_tuple = []
	for player in pos_list:
		player_tuple = {"name":player.name, "avg": player.avg, "std":player.std, 
		"tier":player.tier, "rank":player.rank, "inverserank":1/player.rank}
		
		result.append(player_tuple)

	return result


def tiers(pos_list):
	tier = 1
	prevavg = pos_list[0].avg
	for x in pos_list:
		if (x.avg - prevavg) > 3:
			tier = tier+1
			prevavg = x.avg
			x.tier = tier
		else:
			x.tier = tier
	for playa in pos_list:
		gap = int(25 / tier)
		playa.tier = 30 - gap*(playa.tier-1)
	return pos_list

