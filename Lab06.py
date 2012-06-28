from datetime import date
class Player:
    def __init__(self,firstname,lastname,team):
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
    
torres=Player('fernando','torres','spain')
ronaldo=Player('Ronaldo','yet','portugal')

torres.add_score(date.today(),0)
torres.add_score(date.today(),0)
torres.add_score(date.today(),1)
torres.add_score(date.today(),0)
torres.add_score(date.today(),1)
torres.average_score()
torres.average_score()


class Team:
    def __init__(self,name,league,manager_name,points):
        self.name=name
        self.manager_name=manager_name
        self.league=league
        self.points=points
        self.Players=[]
    def add_player(self,Player):
        self.Players.append(Player)
    def __str__(self):
       description=self.name + ' has '+ str(self.points) + ' points'
       return description

portugal=Team('portugal','euro 2012','i dont knw ',26)
spain=Team('spain','euro 2012','i dont know',78)
spain.add_player(torres)
portugal.add_player(ronaldo)
portugal







class Match:
    def __init__(self,home_team,away_team,date):
             self.home_team=home_team
             self.away_team=away_team
             self.date=date
             self.home_score={'torres':8}
             self.away_score={}
    def home_scores(self):
        sum_home_scores=sum(self.home_score.values)
        return self.sum_home_scores
        
    def away_scores(self):
        sum_away_scores=sum(self.home_score.values)
        return self.sum_away_scores
    def winner_scores(self):
        sum_home=sum(self.home_score.values())
        sum_away=sum(self.away_score.values())
        if sum_home >sum_away:
            return self.home_team
        elif sum_home ==sum_away:
            return 'draw'
        elif sum_home < sum_away:
            return self.away_team
    def add_score(self,Player,score):
        self.team=Player.team
        if self.team==self.home_team:
            self.home_score={Player:score}
        else:
            self.away_score={Player:score}
            
euro_semi_final=Match('spain','portugal',date(2012,6,23))
euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(ronaldo,0)
euro_semi_final.add_score(torres,6)
euro_semi_final.add_score(ronaldo,0)
print 'The winner is ', euro_semi_final.winner_scores()


        


