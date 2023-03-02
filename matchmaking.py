import random

# Fill this out with values from 0 - 100
rank = {
    'rickey': 0, 
    'chad': 0, 
    'james': 0, 
    'mike': 0, 
    'kevin': 0, 
    'yi': 0, 
    'jeb': 0,
    'zach': 0, 
    'alan': 0, 
    'tim': 0, 
    'eric': 0, 
    'josh': 0, 
    'stephen': 0, 
    'dennis': 0, 
}

def inhouse_team_matchmaking(participants):
    DIFFERENTIAL = 10 # Will use to account for some leeway when averaging out scores

    if len(participants) != 10:
        return 'Error: Invalid player count'

    avg_lvl = get_total_level_participants(participants) / 2

    # Randomly split everyone into two teams
    t1_lvl, t2_lvl = 0, 0
    # count = 0 # for testing to make sure the loop doesnt go crazy

    while(t1_lvl > avg_lvl + DIFFERENTIAL or t2_lvl > avg_lvl + DIFFERENTIAL  or t1_lvl == 0):    
        random.shuffle(participants)
        t1_lvl = get_total_level_participants(participants[0:5])
        t2_lvl = get_total_level_participants(participants[5:])
        # count += 1

    print('team 1: (' + str(t1_lvl) + ') ' + str(participants[0:5]))
    print('team 2: (' + str(t2_lvl) + ') ' + str(participants[5:]))
    return participants
    
def get_total_level_participants(participants):
    total = 0
    for p in participants:
        if p not in rank:
            return 'Player not found in rankings'
        total += rank[p]
    return total

# Just for testing
def generate_random_ten():
    players = list(rank.keys())
    random.shuffle(players)
    return players[0:10]

if __name__ == "__main__":
    i = 0
    while i < 10:
        inhouse_team_matchmaking(generate_random_ten())
        print(' ')
        i += 1
    