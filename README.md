
**Beerpong Predicting**
Beerpong Predicting is a Python-based simulator designed to calculate odds for various events in a beerpong game. By simulating millions of matches, the tool provides probabilities for different outcomes based on player accuracies. This project is ideal for anyone interested in game simulations, probability calculations, or just having some fun with data.

Features
Simulate Beerpong Games: Input player accuracies for two teams and simulate matches to calculate odds.
Odds Calculated:
First team to toss the ball
First team to hit a cup
Total tosses (over/under)
Custom Margins: Override the calculated odds with specific margins to optimize for different scenarios or maximize profits.
Planned Features
Profit Calculations: Incorporate profit estimations based on the number of players and average bet amounts.
Advanced Odds: Extend the range of events and scenarios for which odds can be calculated.
Graphical User Interface (GUI): Develop a user-friendly interface to make the tool more accessible.
Web Integration: Deploy the tool on a website where users can easily see and interact with the calculated odds.
Tournament Mode: Add features to simulate entire beerpong tournaments, complete with bracket generation and match tracking.
Usage:

Install Dependencies:
Make sure you have Python installed. Then, install any required libraries using pip:

pip install -r requirements.txt
Input Player Data:
Edit the player_data.json file (or whichever method you use) to input the accuracies for each team. The format should be clear and easy to understand:


To run the code you just run test_for_simulate.py

To add overrun (margin) you need to change the margin parameter.

If you wish to run more or less simulations, you can change num_games (in beerpong_odds_calc.py)

To change player accuracies you can change them in test_for_simulate.py currently only 2v2 games are supported.


Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

Future Goals
Although a GUI is planned for future development, the current focus is on expanding the range of scenarios for odds calculation and refining the accuracy of the simulation. Stay tuned for updates!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

