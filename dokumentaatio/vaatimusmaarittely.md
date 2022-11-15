# Requirement Specification

Scrabble is a classic crossword-like boardgame, my application intends to simulate this on a computer. There are two modes of play, you can play against computers that have varying levels of skill or you can do local hotseat game, where one player takes a turn and then looks away while the other player plays his turn. I intend to also implement a highscore board that displays at the end of the game or by navigating to it in the main menu. 

## Requirements

* A player can play against another player in a hotseat manner.
* A player can play against computers with different degrees of skill.
* The program will have a interactive graphical board and menu.
* The program will use a fast dictionary lookup method to validate word constructions.
* Several official dictionaries shall be available, including a few non-english ones. 
* The application shall announce if your word is legitamate or not, if it isn't legitamate the turn will not end.
* When a player or computer constructs a legitamate word they shall be given points dependent on the points of the letters and the placement of the word on the board, so the game will include Double letter, Triple letter, Double word, Triple word, Start tiles.
* A highscore board can be seen at the end of a game and in the main menu.
* Players can resign, adjourn the game with the click of a button.
* PLayers have the option of having a timer, the player looses if it runs out and the other player or computer has a higher score.
* The other player or computer can play the rest of their turns, if they have less points than the player who ran out of time the latter wins and if they have managed to collect more points in the span of their turns they win, they also win instantly when they get more points than the player who ran out of time.

