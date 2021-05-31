# rock-paper-scissors-exercise
Game- Assignment #1 

This repo contains a basic command-line game of rock-paper-scissors. 
## Installation
Clone or download this repo onto your local computer.
Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

cd /c/Python\ Exercise/rock-paper-scissors-exercise/
## Setup
Setup a virtual environment (if you like that kind of thing):
```sh
conda create -n my-rps-game-env python=3.8
conda activate my-rps-game-env
```
Install the required packages:
```sh pip install -r requirements.txt 
```

### Configuring Environment Variables
Add a new ".env" file to the root directory of this repo, and place contents like the following inside:
```
PLAYER_NAME="Tammana"
```
## Usage
Run the game:
```sh
python game.py
```

