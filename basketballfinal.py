from pprint import pprint

text = open('NBA Stats 202223 All Stats  NBA Player Props Tool.csv').read().strip()
#---------------------------------------------------------------------------------------------
print('-' * 20 + " Two D List" + '-' * 20)
#function: twodListMaker
#author: Maaruf
#contract: accepts list, returns 2D list
#description: Separates the list into a list per player with their stats
def twodListMaker(s):
    data = []
    lines = s.split('\n')
    lines.pop(0)
    for line in lines:
        data.append(line.split(','))
    for lines in data:
        lines.remove(lines[28])
        lines.remove(lines[27])
        lines.remove(lines[26])
        lines.remove(lines[25])
        lines.remove(lines[24])
        lines.remove(lines[23])
        lines.remove(lines[16])
        lines.remove(lines[15])
        lines.remove(lines[13])
        lines.remove(lines[12])
        lines.remove(lines[11])
        lines.remove(lines[9])
        lines.remove(lines[8])
        lines.remove(lines[7])
        lines.remove(lines[6])
        lines.remove(lines[3])
        lines.remove(lines[0])
    return data

testTwoD = twodListMaker(text)
#pprint(testTwoD)
pprint(testTwoD[:2]) #saves space in the shell

#---------------------------------------------------------------------------------------------
print('-' * 20 + "Team Rosters" + '-' * 20)
#function: team_roster
#author: Maaruf
#contract: accepts a 2D list, returns a dictionary
#description: Creates a dictionary filled with each team's roster.
def team_roster(s):
    Player_Dict = {}
    for lines in s:
        if lines[1] in Player_Dict:
            a = Player_Dict[lines[1]]
            Player_Dict[lines[1]] == a.append(lines[0])
        else:
            Player_Dict[lines[1]] = [lines[0]]
    return Player_Dict

roster = team_roster(testTwoD)
print(roster) #saves space in the shell
#pprint(roster)

#---------------------------------------------------------------------------------------------
print('-' * 20 + "Leading Scorers per Team" + '-' * 20)
#function: leading_team_scorer_dict
#author: Maaruf
#contract: accepts a 2D list, returns a dictionary
#description: filters through each team's players, and returns a dictionary with the highest scorer on that team, along with their points per game
def leading_team_scorer_dict(s):
    leading_scorers = {}
    for lines in s:
        if lines[1] in leading_scorers:
            for key, value in leading_scorers.items():
                if key == lines[1]:
                    if float(value[1]) <= float(lines[6]):
                        leading_scorers[key] = lines[0::6]
        else:
            leading_scorers[lines[1]] = lines[0::6]
    return leading_scorers

pprint(leading_team_scorer_dict(testTwoD))

#---------------------------------------------------------------------------------------------
print('-' * 20 + "Average Points per Game by Team" + '-' * 20)
#function: team_avg_points_dict
#author: Maaruf
#contract: accepts a 2D list, returns a dictioanry
#description: adds up the total amount of points produced by each player on each team,
#             then adds up the total points scored by the team in the season, which is then divided by the number of games
def team_avg_points_dict(s):
    avg_points = {}
    for lines in s:
         if lines[1] in avg_points:
            a = avg_points[lines[1]]
            avg_points[lines[1]] = (a + (float(lines[6]) * float(lines[3])))
         else:
            avg_points[lines[1]] = (float(lines[6]) * float(lines[3]))
    for key, value in avg_points.items():
        avg_points[key] = round((avg_points[key]/82), 2)
    return avg_points

pprint(team_avg_points_dict(testTwoD))
        
#---------------------------------------------------------------------------------------------
print('-' * 20 + "Average Team Age" + '-' * 20)
#function: team_age_dict
#author: Maaruf
#contract: accepts a 2D list, returns a dictionary
#description: Adds up the age of every player per team, then divides by the total number of people on that team
def team_age_dict(s):
    team_age = {}
    for lines in s:
        if lines[1] in team_age:
            a = team_age[lines[1]]
            team_age[lines[1]] == a.append(float(lines[2]))
        else:
            team_age[lines[1]] = [(float(lines[2]))]
    for key, values in team_age.items():
         team_age[key] = str(round((sum(team_age[key]) / len(team_age[key])), 2)) + ' years old on average'
    return team_age

age_dict = team_age_dict(testTwoD)
pprint(age_dict)
    