import random

def simulate_game(team1, team2, player_accuracies):
    cups_team1 = 10
    cups_team2 = 10

    tosses_team1 = 0
    tosses_team2 = 0

    # Randomly select the team to start
    start_team = random.choice([1, 2])

    if start_team == 1:
        current_team = team1
        opposing_team = team2
    else:
        current_team = team2
        opposing_team = team1

    results = {}  # {'winner': 'team', 'first_toss': 'team', 'first_cup_hit': 'team'}
    first_cup_flag = True

    turn = 0
    while cups_team1 > 0 and cups_team2 > 0:
        # Determine the current player within the current team
        current_player = current_team[turn % 2]
        accuracy = player_accuracies[current_player]

        # Simulate the shot
        if random.random() < accuracy:
            if current_team == team1:
                cups_team2 -= 1
                tosses_team1 += 1
                if first_cup_flag:
                    results['first_cup_hit'] = 'team1'
                    first_cup_flag = False
            else:
                cups_team1 -= 1
                tosses_team2 += 1
                if first_cup_flag:
                    results['first_cup_hit'] = 'team2'
                    first_cup_flag = False

            # Swap teams after a successful shot
            current_team, opposing_team = opposing_team, current_team
        else:
            # Missed shot, simply count the toss
            if current_team == team1:
                tosses_team1 += 1
            else:
                tosses_team2 += 1

            # Swap teams after a missed shot as well
            current_team, opposing_team = opposing_team, current_team

        turn += 1

    # Determine the winner
    if cups_team1 == 0:
        results['winner'] = 'team2'
    else:
        results['winner'] = 'team1'

    results['total_tosses_team1'] = tosses_team1
    results['total_tosses_team2'] = tosses_team2

    results['team1_total_cups_left'] = cups_team1
    results['team2_total_cups_left'] = cups_team2

    results['first_toss'] = 'team1' if start_team == 1 else 'team2'

    return results

# Define player accuracies (probability of making a shot)
player_accuracies = {
    'Player1': 0.2,
    'Player2': 0.5,
    'Player3': 0.5,
    'Player4': 0.5,
}

# Define teams
team1 = ['Player1', 'Player2']
team2 = ['Player3', 'Player4']

# Simulate 1000 games
games = 100000
team1_wins = 0
team2_wins = 0
total_tosses_team1 = 0
total_tosses_team2 = 0
first_cup_hit_team1 = 0
first_cup_hit_team2 = 0

for _ in range(games):
    result = simulate_game(team1, team2, player_accuracies)
    
    if result['winner'] == 'team1':
        team1_wins += 1
    else:
        team2_wins += 1

    total_tosses_team1 += result['total_tosses_team1']
    total_tosses_team2 += result['total_tosses_team2']
    
    if result['first_cup_hit'] == 'team1':
        first_cup_hit_team1 += 1
    else:
        first_cup_hit_team2 += 1

# Calculate and print statistics
print(f"Team 1 Wins: {team1_wins} ({team1_wins/games*100:.2f}%)")
print(f"Team 2 Wins: {team2_wins} ({team2_wins/games*100:.2f}%)")
print(f"Average Tosses by Team 1: {total_tosses_team1/games:.2f}")
print(f"Average Tosses by Team 2: {total_tosses_team2/games:.2f}")
print(f"First Cup Hit by Team 1: {first_cup_hit_team1} times ({first_cup_hit_team1/games*100:.2f}%)")
print(f"First Cup Hit by Team 2: {first_cup_hit_team2} times ({first_cup_hit_team2/games*100:.2f}%)")
