import random

# Define player accuracies (probability of making a shot)
player_accuracies = {
    'Player1': 0.27,
    'Player2': 0.35,
    'Player3': 0.41,
    'Player4': 0.24,
}

# Define teams
team1 = ['Player1', 'Player2']
team2 = ['Player3', 'Player4']

# Simulate a single game
def simulate_game(team1, team2, player_accuracies):
    cups_team1 = 10
    cups_team2 = 10
    players = team1 + team2
    turn = 0

    #we need to make sure its a random team that starts each time
    #first we pick a team to start
    start_team = random.choice([1, 2])

    if start_team == 1:
        players_order = team1 + team2
    else:
        players_order = team2 + team1



    while cups_team1 > 0 and cups_team2 > 0:
        current_player = players_order[turn % len(players_order)]
        accuracy = player_accuracies[current_player]
        if random.random() < accuracy:
            if current_player in team1:
                cups_team2 -= 1
            else:
                cups_team1 -= 1
        turn += 1

    return 1 if cups_team2 == 0 else 2

# Simulate multiple games
def simulate_multiple_games(num_games, team1, team2, player_accuracies):
    wins_team1 = 0
    wins_team2 = 0
    game_num = 0

    for _ in range(num_games):
        print(f"{game_num}/{num_games}")
        game_num += 1


        result = simulate_game(team1, team2, player_accuracies)
        if result == 1:
            wins_team1 += 1
        else:
            wins_team2 += 1

    
    return wins_team1, wins_team2

def calculate_odds(team1_wins, team2_wins, number_games, margin):
    # Calculate raw probabilities
    chance_team1 = team1_wins / number_games
    chance_team2 = team2_wins / number_games

    odds_team1 = margin / chance_team1
    odds_team2 = margin / chance_team2

    odds_team1 = round(odds_team1, 2)
    odds_team2 = round(odds_team2, 2)

    if odds_team1 < 1:
        odds_team1 = 1.01
    if odds_team2 < 1:
        odds_team2 = 1.01


    return odds_team1, odds_team2

# Number of simulations
num_games = 100000
margin = 0.90  # overrun as a decimal

# Run the simulations
wins_team1, wins_team2 = simulate_multiple_games(num_games, team1, team2, player_accuracies)

# Calculate odds
odds_team1, odds_team2 = calculate_odds(wins_team1, wins_team2, num_games, margin)

# Calculate and print results
print(f"Team 1 wins: {wins_team1} times ({wins_team1 / num_games * 100:.2f}%)")
print(f"Team 2 wins: {wins_team2} times ({wins_team2 / num_games * 100:.2f}%)")

# Print the odds
print(f"Odds for Team 1 = {odds_team1}")
print(f"Odds for Team 2 = {odds_team2}")
