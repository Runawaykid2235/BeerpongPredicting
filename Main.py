import random


class SimulateGames:
    """
    A class to simulate beerpong games and calculate/sum up various elements and statistics    
    """

    def __init__(self, team1, team2, player_accuracies):
        self.team1 = team1
        self.team2 = team2
        self.player_accuracies = player_accuracies


    @staticmethod
    def simulate_game(team1, team2, player_accuracies):
        """
        Simulate a single game between two teams.

        Args:
            team1 (list): list of players in team1.
            team2 (list): listof players in team2.
            player_accuracies (dictionary): A dictionary of playernames and their beerpong shot accuracy

        Returns:
            a dictionary with game results including winner, total tosses and remaining cups
        """
    
        #need to tally each game how many throwsfor over under fixing odds
    
        cups_team1 = 10
        cups_team2 = 10
        critical_shots = 0

        cups_hit_pr_player = {'Player1': 0, 'Player2': 0, 'Player3': 0, 'Player4': 0}

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
                    cups_hit_pr_player[current_player] += 1


                    cups_team2 -= 1
                    tosses_team1 += 1
                    if first_cup_flag:
                        results['first_cup_hit'] = 'team1'
                        first_cup_flag = False
                else:
                    cups_hit_pr_player[current_player] += 1
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

        results['nested_player_cups_hit_dict'] = cups_hit_pr_player

        results['total_tosses_team1'] = tosses_team1
        results['total_tosses_team2'] = tosses_team2

        results['team1_total_cups_left'] = cups_team1
        results['team2_total_cups_left'] = cups_team2
        
        #add how many critical shots were took
        results['total_critical_shots'] = critical_shots

        results['first_toss'] = 'team1' if start_team == 1 else 'team2'

        return results


    @staticmethod
    def simulate_multiple_games(num_games, team1, team2, player_accuracies):
        """
        Simulate multiple games between two teams
        
        Args:
            num_games (int): Number of games to simulate.
            team1 (list): List of players in team1.
            team2 (list): list of players in team2.
            player_accuracies (dict): A dictionayry mappingplayer names to their accuracy in beerpong

        Returns:
            A dict containing statistics from all simulated games (contains nested dicts)
        """
        

        
        game_num = 0
        tally = {
            'total_tosses_team1': 0,
            'total_tosses_team2': 0,
            'team1_total_cups_left': 0,
            'team2_total_cups_left': 0,
            'total_critical_shots': 0,
            'total_wins_team1': 0,
            'total_wins_team2': 0,
            'under_10_tosses': 0,
            'cups_hit_pr_player': {
                'Player1': 0,
                'Player2': 0,
                'Player3': 0,
                'Player4': 0
                }
        }

        categories_for_over_under_tosses_team1 = {
            10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 
            20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 
            30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 
            40: 0
        }


        categories_for_over_under_tosses_team2 = {
            10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 
            20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 
            30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 
            40: 0
        }

        categories_for_over_under_cups_left_team1 = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        categories_for_over_under_cups_left_team2 = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}


        #add the categories for over under tosses to the tally dict
        tally['categories_for_over_under_tosses_nested_team1'] = categories_for_over_under_tosses_team1
        tally['categories_for_over_under_tosses_nested_team2'] = categories_for_over_under_tosses_team2

        #add the categories for over under cups left
        tally['categories_for_over_under_cups_left_nested_team1'] = categories_for_over_under_cups_left_team1
        tally['categories_for_over_under_cups_left_nested_team2'] = categories_for_over_under_cups_left_team2
        
        

        for _ in range(num_games):
            print(f"{game_num}/{num_games} {round(game_num / num_games * 100)}%")
            game_num += 1

            result = SimulateGames.simulate_game(team1, team2, player_accuracies)

            # Update numerical values
            if result.get('winner') == 'team1':
                tally['total_wins_team1'] += 1 
            else:
                tally['total_wins_team2'] += 1
            

            #implement over under total tosses by arranging them in categories like 10 or below, 11, 12, 13, so on
            tally['total_tosses_team1'] += result.get('total_tosses_team1', 0)
            tally['total_tosses_team2'] += result.get('total_tosses_team2', 0)


            total_tosses_team1 = result.get('total_tosses_team1')
            total_tosses_team2 = result.get('total_tosses_team2')

            total_cups_left_team1 = result.get('team1_total_cups_left')
            total_cups_left_team2 = result.get('team2_total_cups_left')
            

            if total_tosses_team1 in categories_for_over_under_tosses_team1:
                # Increment the corresponding value by 1
                tally['categories_for_over_under_tosses_nested_team1'][total_tosses_team1] += 1


            if total_tosses_team2 in categories_for_over_under_tosses_team2:
                # Increment the corresponding value by 1
                tally['categories_for_over_under_tosses_nested_team2'][total_tosses_team2] += 1


            if total_cups_left_team1 in categories_for_over_under_cups_left_team1:
                tally['categories_for_over_under_cups_left_nested_team1'][total_cups_left_team1] += 1

            if total_cups_left_team2 in categories_for_over_under_cups_left_team2:
                tally['categories_for_over_under_cups_left_nested_team2'][total_cups_left_team2] += 1



            tally['total_tosses_team2'] += result.get('total_tosses_team2', 0)
            tally['team1_total_cups_left'] += result.get('team1_total_cups_left', 0)
            tally['team2_total_cups_left'] += result.get('team2_total_cups_left', 0)
            tally['total_critical_shots'] += result.get('total_critical_shots', 0)

            for player, hits in result['nested_player_cups_hit_dict'].items():
                tally['cups_hit_pr_player'][player] += hits

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
    """ A class to calculate various odds """

    @staticmethod
    def calculate_winner_odds(results, number_games, margin):
        """
        Calculate team to win

        Args:
            results (dict): A list off various stats from the simulated games. Specifically we need team1 total winnings and team2 total wins.
            number_games(int): How many games where simulated from the class SimulateGames
            Margin(int): Margin is the overrun of the odds. We lower odds to make us more profitable.
        """

        #so we recieve the game results as a dict like {'total_tosses_team1': 19160, 'total_tosses_team2': 195369, 'team1_total_cups_left': 3397, 'team2_total_cups_left': 33300, 'total_critical_shots': 23861, 'average_tosses_team1_pr_game': 19.186, 'average_tosses_team2_pr_game': 19.5369, 'average_cups_left_team1_pr_game': 0.3397, 'average_cups_left_team2_pr_game': 3.33, 'averaged_critical_shots': 2.3861, 'total_average_tosses': 38.7229, 'average_cups_left': 3.6697}    
        team1_wins = results.get('total_wins_team1', 0)
        team2_wins = results.get('total_wins_team2', 0)

        #the first odds for win team1 or team2
        chance_team1 = team1_wins / number_games
        chance_team2 = team2_wins / number_games

        if chance_team1 == 0:
            chance_team1 += 0.0001

        if chance_team2 == 0:
            chance_team2 += 0.0001
            

        odds_team1 = margin / chance_team1
        odds_team2 = margin / chance_team2

        odds_team1 = round(odds_team1, 2)
        odds_team2 = round(odds_team2, 2)

        if odds_team1 < 1:
            odds_team1 = 1.01
        if odds_team2 < 1:
            odds_team2 = 1.01


        return  f"odds team1 = {odds_team1}  -  odds team2 = {odds_team2}"
    

    @staticmethod
    def calculate_over_under_cups(results, number_games, margin):
        """
        Calculate team to win

        Args:
            results (dict): A list off various stats from the simulated games. Specifically we need a dict with how many times there was 1 cup left, 2 cup left so on.
            number_games(int): How many games where simulated from the class SimulateGames
            Margin(int): Margin is the overrun of the odds. We lower odds to make us more profitable.
        """

        # Extract dictionaries for cups left
        team1_cups_left_dict = results['categories_for_over_under_cups_left_nested_team1']
        team2_cups_left_dict = results['categories_for_over_under_cups_left_nested_team2']

        # Convert counts to percentages
        for cat in team1_cups_left_dict:
            team1_cups_left_dict[cat] = (team1_cups_left_dict[cat] / number_games) * 100

        for cat in team2_cups_left_dict:
            team2_cups_left_dict[cat] = (team2_cups_left_dict[cat] / number_games) * 100

        under_odds_team1 = {}
        over_odds_team1 = {}

        under_odds_team2 = {}
        over_odds_team2 = {}


        for key in team1_cups_left_dict:
            current_under_total = 0

            for num in team1_cups_left_dict:
                if num < key:
                    current_under_total += team1_cups_left_dict[num]
                under_odds_team1[key] = round((margin / (current_under_total + 0.000001)) * 100, 2)


        for key in team1_cups_left_dict:
            current_over_total = 0

            for num in team1_cups_left_dict:
                if num > key:
                    current_over_total += team1_cups_left_dict[num]
                over_odds_team1[key] =  round((margin / (current_over_total + 0.000001)) * 100, 2)


        for key in team2_cups_left_dict:
            current_under_total = 0

            for num in team2_cups_left_dict:
                if num < key:
                    current_under_total += team2_cups_left_dict[num]
                under_odds_team2[key] =  round((margin / (current_under_total + 0.000001)) * 100, 2)

        for key in team2_cups_left_dict:
            current_over_total = 0

            for num in team2_cups_left_dict:
                if num > key:
                    current_over_total += team2_cups_left_dict[num]
                over_odds_team2[key] =  round((margin / (current_over_total + 0.000001)) * 100, 2)

                

        return f"under_odds_team1: {under_odds_team1}, over_odds_team1: {over_odds_team1}, under_odds_team2: {under_odds_team2}, over_odds_team2: {over_odds_team2}"


    @staticmethod
    def calculate_over_under_throws(results,number_games, margin):
        """
        Calculate team to win

        Args:
            results (dict): A list off various stats from the simulated games. Specifically we need a dict with how many times there was 1 cup left, 2 cup left so on.
            number_games(int): How many games where simulated from the class SimulateGames
            Margin(int): Margin is the overrun of the odds. We lower odds to make us more profitable.
        """


        #now to calculate overunder throws its alot like calculating the over under cups left, but we might want to do total tosses
        # Extract dictionaries for cups left
        team1_tosses = results['categories_for_over_under_cups_left_nested_team1']
        team2_tosses = results['categories_for_over_under_cups_left_nested_team2']

        total_team_tosses = {}

        # Summing up the tosses
        for key in team1_tosses:
            if key in team2_tosses:
                total_team_tosses[key] = team1_tosses[key] + team2_tosses[key]
            else:
                total_team_tosses[key] = team1_tosses[key]

        for key in team2_tosses:
            if key not in total_team_tosses:
                total_team_tosses[key] = team2_tosses[key]

        # Convert counts to percentages
        for cat in total_team_tosses:
            total_team_tosses[cat] = (total_team_tosses[cat] / number_games) * 100

        under_odds = {}
        over_odds = {}

        # Calculate under odds
        for key in total_team_tosses:
            current_under_total = 0
            for num in total_team_tosses:
                if num < key:
                    current_under_total += total_team_tosses[num]
            if current_under_total > 0:
                under_odds[key] = round((margin / current_under_total) * 100, 2)
            else:
                under_odds[key] = float('inf')  # or some other indicator for no data

        # Calculate over odds
        for key in total_team_tosses:
            current_over_total = 0
            for num in total_team_tosses:
                if num > key:
                    current_over_total += total_team_tosses[num]
            if current_over_total > 0:
                over_odds[key] = round((margin / current_over_total) * 100, 2)
            else:
                over_odds[key] = float('inf')  # or some other indicator for no data


        return f"total over tosses in game: {over_odds}, total under tosses in game: {under_odds}"

    @staticmethod
    def calculate_MVP(results, number_games, margin):
        """ Function to calculate odds for the man of the match, or the most valuable player """
        #the mvp of a match is the player who hits the most cups
        #get player stats
        player_hits = results['cups_hit_pr_player']

        total = 0

        for key in player_hits:
            total += player_hits[key]

        #calculate percentage
        for key in player_hits:
            player_hits[key] = player_hits[key] / total * 100

        #convert to decimal odds
        for key in player_hits:
            player_hits[key] = round((margin / player_hits[key]) * 100, 2)

        return player_hits


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


# Example: Plotting the average cups left per game for each team
labels = ['Team 1', 'Team 2']
average_cups_left = [
    results['average_cups_left_team1_pr_game'],
    results['average_cups_left_team2_pr_game']
]


#overrun is how much margin we allow us (bookmaker)to have
overrun = 0.80


results_odds = OddsCalculator.calculate_winner_odds(results, num_games, overrun)
over_under_cups = OddsCalculator.calculate_over_under_cups(results, num_games, overrun)
over_under_throws = OddsCalculator.calculate_over_under_throws(results, num_games, overrun)
mvp_odds = OddsCalculator.calculate_MVP(results, num_games, overrun)


print(f"result odds = {results_odds}")
print(f"over under cups = {over_under_cups}")
print(f"over under throws = {over_under_throws}")
print(f"mvp odds = {mvp_odds}")