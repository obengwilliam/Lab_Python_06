from datetime import date

class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team
    def add_score(self,date,score):
        self.scores.append(score)
    def total_score(self):
        return sum(self.scores)
    def average_score(self):
        return (sum(self.scores)/float(len(self.scores)))


torres=Player('fernando','torres')
torres.add_score(date.today(),0)
torres.add_score(date.today(),0)
torres.add_score(date.today(),1)
torres.add_score(date.today(),0)
torres.add_score(date.today(),1)

print torres.average_score()


class Team:
    def __init__(self,name,league,manager_name,points):
        self.name=name
        self.manager_name=manager_name
        self.league=league
        self.points=points
    def add_player(self,Player):
        self.Player=Player
        
