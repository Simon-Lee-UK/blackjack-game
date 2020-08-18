# Python Blackjack Game
>A text-based Blackjack game written in Python.  

Recently, I've spent a lot of time with pandas in Jupyter Notebooks. This project provided an excellent excuse to 
revisit Python's core functionality and focus on principles of object-oriented programming whilst building something 
fun. Along the way: I tried-out the pytest framework (it's great); kept everything modular and extensible; brought 
dedication to documentation and have lost huge sums of virtual money to the game's dealer.  
  
Credit to [Alex Large](https://github.com/alexanderklarge) who inspired this project by starting his own Blackjack game. 
It got me thinking about how I'd approach the task and before I knew it, this repository was born. Give the game a go, 
instructions to get started can be found below; one day I'll come back and add a GUI...

<p align="center">
  <img src="https://github.com/Simon-Lee-UK/image-repository/blob/master/blackjack-game/blackjack_gameplay_composite.png"
  alt="Blackjack gameplay examples"
  width="900">
</p>

## Getting Started
1\. Clone or download the repository:
```bash
git clone https://github.com/Simon-Lee-UK/blackjack-game.git  # Grabs the code from GitHub
cd blackjack-game  # Navigates into the top level of the repository
```

2\. Using the [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) environment and package 
manager, install the environment required to run the game and associated set of tests. First, create the environment 
from the `environment.yml` file:
```bash
conda env create -f environment.yml
```
Next, activate the newly created environment:
```bash
conda activate blackjack-dev
```

3\. Finally, run the game package from the repository root:
```bash
python -m blackjack
```

If you're not familiar with the game of Blackjack, an excellent set of rules can be found here:
https://bicyclecards.com/how-to-play/blackjack/

## Tests
Unit tests use the [pytest](https://docs.pytest.org/en/stable/) framework. Run all tests using:
```bash
python -m pytest
```  
  
## Extensions
- Extend gameplay with additional Blackjack actions: 'splitting pairs', 'doubling down', 'insurance', etc.
- Add support for multiple human players.
- Add a graphical user interface to the game.
- Refactoring:
    - Update the return values of some methods (especially on the hand classes/subclasses) to either return data that is 
    then e.g. printed by the caller or to return a suitable status code. Aim to protect current data encapsulation and 
    abstraction while facilitating the writing of better unit tests incl. initial-/final-state tests across single 
    rounds with fully mocked-out player and dealer hands.
    - Extend inheritance and polymorphism to the card class? Aces have suitably different behaviour that they may 
    benefit from specialised methods.
- Create StatJack: an agent that repeatedly plays rounds of the game with pseudo-random inputs, generating a large 
dataset of outcomes linked to initial/intermediate conditions and player actions.
- Train a ML agent to play (basing the reward function on long-term balance as opposed to rounds won); compare to 
results of visualised from StatJack; trained agent could play alongside human players.
  
## License
The code in this project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). 
See [LICENSE.txt](./LICENSE.txt) for details.
