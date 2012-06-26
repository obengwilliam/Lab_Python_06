"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/22/2012	| 1
"""

## create the player_stats data structure
from  datetime import date
s=date(2012,6,23)
t=date(2012,6,25)
u=date(2012,6,19)
y=date(2012,6,20)
f=date(2012,6,21)
k=date(2012,6,22)

player_stats={'rooney':[(s,2),(t,2)],
              'ronaldo':[(u,0),(y,3)],
              'torres':[(f,0),(k,1)]}


## implement highest_score

def highest_score(x):
    score=[]
    for name in x:
        for j in x[name]:
            score.append(j[1])
    for name in x:
        if x[name][1][1]==max(score):
           return name,x[name][1][0],x[name][1][1]
    print name,max(score)       
        



    
#highest_score(player_stats)
def highest_score(x,player):
    names=x.keys()
    if player in names:
       ma=[]
       for i in x[player]:
           ma.append(i[1])
       return 'This is ',player,'highest score:',max(ma)
           
    else:
        return 'does not exist'

        


## implement highest_score_for_player



## implement highest_scorer
def highest_score(x):
    highest=[]
    for name in x:
        highest.append(x[name][0][1]+ x[name][1][1])
        
    return max(highest)   
print highest_score(player_stats)
 
