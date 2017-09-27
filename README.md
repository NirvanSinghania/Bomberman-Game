BOMBERMAN GAME

The game has been implemented using python 2.7.
For rendering colours to  the text displayed, the termcolor library has been imported
The game has 3 levels and the bomberman will have 3 lives . 

Instruction to run the game:

python run.py

Game Controls :
 w - up
 a - left
 s - down
 d - right
 b - plant bomb
 q - quit

 Implementation:

 The code has been divided into a number of different modules creating classes for a number of identities
 thus rendering MODULARITY.

 The various files are-

 game_board.py - It consists of a class board which consists of all the features required as a member variables.
 It is responsible for the matrix printed on the screen and provides an interface for various entities.
 There are two matrices one of numbers for various ientities,M and one with 4 characters/symbols for a grid for
 printing purpose.

 input_output.py - Provides the function for taking input with facility to wait for i/o efficiently using the 
 select module in python
 
 config.py - Contains some constants defined and instructions for printing every symbol with respective colour.
 
 persons.py - A Base class Person with basic coordinates as variables and member functions for movement. Also functions 
 to handle kill of the person example clear for filling the position of the curret person with air ec

 hero_enemy.py - It has two classes Hero and Enemy both inherited from Person . Hero handles movement of bomerman,killing of bomerman and also the his score, while Enemy class is for object enemy with specific functions for RANDOM movement of enemy and different definitions of kill.The code involves use of private variable  __score in Hero class and member functions to access it. Also in the Enemy class the kill function of parent is overrided to render a new function.

 bomb.py - Class Bomb . Handles the creation of bomb and entities affected due to explosion. It also has a private variable counter which decides the phases of the bomb creation,explosion and end and a master function to call these procedures based on the value of the counter .

 run.py - This is the main file to run the game .There are two while loop one for the levels and the other for each level.
 It involves a number of checks acting as listeners for events like deletion of all enemies,end of all lives,completion of all levels and clicking of a key. Also in every level one advances the number of enemies increases and the frame time are decreased for increasing the difficulty level.



