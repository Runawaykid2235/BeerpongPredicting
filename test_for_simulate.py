import random

def simulate_game(team1, team2, player_accuracies):
    cups_team1 = 10
    cups_team2 = 10
    turn = 0

    # Randomly select the team to start
    start_team = random.choice([1, 2])

    if start_team == 1:
        players_order = team1 + team2
    else:
        players_order = team2 + team1

    results = {}  # {'winner': 'team', 'first_toss': 'team', 'first_cup_hit': 'team'}
    first_cup_flag = True

    while cups_team1 > 0 and cups_team2 > 0:
        current_player = players_order[turn % len(players_order)]
        accuracy = player_accuracies[current_player]

        if random.random() < accuracy:
            if current_player in team1:
                cups_team2 -= 1
                if first_cup_flag:
                    results['first_cup_hit'] = 'team1'
                    first_cup_flag = False
            else:
                cups_team1 -= 1
                if first_cup_flag:
                    results['first_cup_hit'] = 'team2'
                    first_cup_flag = False

        turn += 1

    if cups_team1 == 0:
        results['winner'] = 'team2'
    else:
        results['winner'] = 'team1'

    results['first_toss'] = 'team1' if start_team == 1 else 'team2'

    return results

# Define player accuracies (probability of making a shot)
player_accuracies = {
    'Player1': 0.5,
    'Player2': 0.5,
    'Player3': 0.5,
    'Player4': 0.5,
}

# Define teams
team1 = ['Player1', 'Player2']
team2 = ['Player3', 'Player4']

# Simulate a game
result = simulate_game(team1, team2, player_accuracies)
print(result)
