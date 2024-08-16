import random
import matplotlib.pyplot as plt


class SimulateGames:
    def simulate_game(team1, team2, player_accuracies):
        cups_team1 = 10
        cups_team2 = 10
        critical_shots = 0

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
            
            if current_team == team1 and cups_team2 == 1 or current_team == team2 and cups_team1 == 1:
                #introducing a critical hit factor, so players perform worse on last shot because of pressure
                accuracy -= 0.05 # perform 5% worse when in critical shot
                critical_shots += 1


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
        
        #add how many critical shots were took
        results['total_critical_shots'] = critical_shots

        results['first_toss'] = 'team1' if start_team == 1 else 'team2'

        return results



    def simulate_multiple_games(num_games, team1, team2, player_accuracies):
        game_num = 0
        tally = {
            'total_tosses_team1': 0,
            'total_tosses_team2': 0,
            'team1_total_cups_left': 0,
            'team2_total_cups_left': 0,
            'total_critical_shots': 0,
            'total_wins_team1': 0,
            'total_wins_team2': 0
        }

        for _ in range(num_games):
            print(f"{game_num}/{num_games} {round(game_num / num_games * 100)}%")
            game_num += 1

            result = SimulateGames.simulate_game(team1, team2, player_accuracies)

            # Update numerical values
            if result.get('winner') == 'team1':
                tally['total_wins_team1'] += 1 
            else:
                tally['total_wins_team2'] += 1
            
            
            
            
            tally['total_tosses_team1'] += result.get('total_tosses_team1', 0)
            tally['total_tosses_team2'] += result.get('total_tosses_team2', 0)
            tally['team1_total_cups_left'] += result.get('team1_total_cups_left', 0)
            tally['team2_total_cups_left'] += result.get('team2_total_cups_left', 0)
            tally['total_critical_shots'] += result.get('total_critical_shots', 0)

            #add some averages
            tally['average_tosses_team1_pr_game'] = tally['total_tosses_team1'] / num_games
            tally['average_tosses_team2_pr_game'] = tally['total_tosses_team2'] / num_games
            
            tally['average_cups_left_team1_pr_game'] = tally['team1_total_cups_left'] / num_games
            tally['average_cups_left_team2_pr_game'] = tally['team2_total_cups_left'] / num_games

            tally['averaged_critical_shots'] = tally['total_critical_shots'] / num_games
            
            #adding total tosses odds to later provide over under total amount of tosses
            tally['total_average_tosses'] = (tally['total_tosses_team1'] + tally['total_tosses_team2']) / num_games
            
            #adding total cups over under 
            #as they are already averaged no need to divide by num_games
            tally['average_cups_left'] = (tally['average_cups_left_team1_pr_game'] + tally['average_cups_left_team2_pr_game'])
            


        return tally



class OddsCalculator:
    def calculate_winner_odds(results, number_games, margin):
        #so we recieve the game results as a dict like {'total_tosses_team1': 191860, 'total_tosses_team2': 195369, 'team1_total_cups_left': 3397, 'team2_total_cups_left': 33300, 'total_critical_shots': 23861, 'average_tosses_team1_pr_game': 19.186, 'average_tosses_team2_pr_game': 19.5369, 'average_cups_left_team1_pr_game': 0.3397, 'average_cups_left_team2_pr_game': 3.33, 'averaged_critical_shots': 2.3861, 'total_average_tosses': 38.7229, 'average_cups_left': 3.6697}    
        team1_wins = results.get('total_wins_team1', 0)
        team2_wins = results.get('total_wins_team2', 0)

        print(team1_wins)
        print(team2_wins)

        #the first odds for win team1 or team2
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


        return  f"odds team1 = {odds_team1}  -  odds team2 = {odds_team2}"






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


num_games = 10000

results = SimulateGames.simulate_multiple_games(num_games, team1, team2, player_accuracies)


print(results)

# Example: Plotting the average cups left per game for each team
labels = ['Team 1', 'Team 2']
average_cups_left = [
    results['average_cups_left_team1_pr_game'],
    results['average_cups_left_team2_pr_game']
]





#overrun is how much margin we allow us (bookmaker)to have
overrun = 0.90


results_odds = OddsCalculator.calculate_winner_odds(results, num_games, overrun)
print(results_odds)



# Create a bar chart
#plt.bar(labels, average_cups_left, color=['red', 'orange'])

# Adding title and labels
#plt.title('Average Cups Left Per Game')
#plt.xlabel('Teams')
#plt.ylabel('Average Cups Left')

# Display the chart
#plt.show()
