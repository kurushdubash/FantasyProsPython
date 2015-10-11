#Defines Player class. Each Player represents a football player with instance variables listing out: 
# 1. Name
# 2. Rank
# 3. Team
# 4. Matchup
# 5. Best rank projected
# 6. Worst rank projected
# 7. Average rank projected. 
# 8. Std. Dev. 
# 9. Week

# Player class: 

class Player: 
	"Player class that represents a football player"

	def __init__(self,name,rank,team,matchup,best,worst,avg,std, week, tier=1):
		"Creates football player"
		self.name = name
		self.rank = rank
		self.team = team
		self.matchup = matchup
		self.best = best
		self.worst = worst
		self.avg = avg
		self.std = std
		self.week = week
		self.tier = tier
		self.labpos = "right"