# Assassin Clue game
It's similar to the board game but different!

## Game description
There are places and weapons
There is a murder that happened by one of the players
Each player has a name, a list of last visited places, and a list
of favorite weapons

## Before the start
The assassin, the victim, the place and weapon of murder are defined.
Also, the visited places are defined, each player must have 1-3 places in their list.
The assassin must visit the place of murder.

Known to the you: the victim, weapon and place of muder
Unknown to all you: the assassin, and what each other player has in their places and weapons lists

## Game play
In each round, you can ONLY suspect 2 other players.

Suspect means: showing randomly 2 visited places, and 1 fav weapon from the suspect.
Then, if you want, you can accuse one of the players

If accusation is correct, you win and game is over.
If not, the game continues, and the next round starts.
In the next round another new player gets killed.
It keeps going until there is only you and the killer, and at this point you lost.
You win by discovering the assassin before all other players are murdered.

## Code structure
We will have the following main components:

- main (solution): It will connect and plug all the other components together
- utils: helper functions
- logger: responsible for getting user input, and printing on the screen
- players: copies of the player class with random list of places and fav weapons
- user: Inherits the player class, but adds to it the ability to "suspect" and "accuse"
- resources: places and weapons, as .json files

## Flow chart
[click here for a better resolution](https://miro.com/app/board/uXjVKfr6auU=/?share_link_id=919883985147)

<img src="flowchart.jpg" alt="drawing" width="600"/>
