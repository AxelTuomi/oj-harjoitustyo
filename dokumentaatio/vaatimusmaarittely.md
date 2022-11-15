# Requirement Specification

Scrabble is a classic crossword-like board-game, my application intends to simulate this on a computer. There are two modes of play, you can play against computers that have varying levels of skill or you can do local Hotseat game, where one player takes a turn and then looks away while the other player plays his turn. I intend to also implement a high-score board that displays at the end of the game or by navigating to it in the main menu.

## Requirements

* A player can play against another player in a Hotseat manner.
* A player can play against computers with different degrees of skill.
* The program will have a interactive graphical board and menu.
* The program will use a fast dictionary lookup method to validate word constructions.
* Several official dictionaries shall be available, including a few non-English ones. 
* The application shall announce if your word is legitimate or not, if it isn't the turn will not end.
* When a player or computer constructs a legitimate word they shall be given points dependent on the points of the letters and the placement of the word on the board, so the game will include Double letter, Triple letter, Double word, Triple word, Start tiles.
* A high-score board can be seen at the end of a game and in the main menu.
* Players can resign, adjourn the game with the click of a button.
* Players have the option of setting a timer between 0-45 minutes, the player looses if it runs out and the other player or computer has a higher score.
* The other player or computer can play the rest of their turns, if they have less points at the end of their played out turns than the player who ran out of time the latter wins and if they have managed to collect more points in the span of their turns they win, they win instantly when they get more points than the player who ran out of time.
* If a player resigns before completing the first turn, the game is aborted and the score is not registered on the high score board.
* The high-score board will be saved to a database after each session.
* The game ends when all letter squares are used unless timers have ran out.
* In the rare case that there are no playable words left with the letters you posses, the game ends for you there.
* There is a bag of 100 letters that the players will use.
* Each player has 7 letters that can be played.
* If the player has less than 7, (which he usually does after a turn) he will draw random letters from the bag, if the bag is not empty.
* Players and computers have the option of using their turn to trade their letters for x amount of random ones drawn from the bag.
* Players and computers can pass their turns .
* At the end the player with a new high score is prompted to write in a name, If a name isn't written in, it will display, playerx (the x being a unique number).

