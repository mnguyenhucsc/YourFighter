https://github.com/mnguyenhucsc/YourFighter
THE README:

The purpose of this class is to have your fighter, say their name, age, height, and move set. Bonus things we can do with this class are things like adding moves and adding nicknames to your fighters.
The Data Variables here are the name, age, height, and their moves. The get_name method would get the name. The get_age method would receive the age. The get_height method would receive the height. The get_moves method has a for loop 
that goes through the list of moves the fighter has. It also contains the word 'and' after the first if statement so when the moves are placed together, they can be seen clearer. The set_name method would add a nickname to your fighter,
changing their name completely. The add_move method adds a move to your fighter's moveset by appending to the next spot in the list of moves. The use_move method prompts the fighter to use one of their moves. If in the main function,
the The_Rock.use_move(*)) has nothing in the parenthesis, the fighter would use a random move based on the randint function. For it to use a specific move, you would input The_Rock.use_move(The People's Smolder)) for it to use it.
If you were to input a move that was not part of their list of movesets, then it would return that the fighter used an 'Invalid Move'.

To use the demo program, you must first list your fighters name (object), i.e The_Rock, then make it equal to the Class name. Then you must list the data variables in order. The moves are put in brackets as they are
part of a list. This would all look like this:
~~Object~~~~~~~~~~Class~~~~~~~~~~~~~Name~~~~~~~~~~~~~~~~~Age~~~~~Height~~~~~~~~~~~Move 1~~~~~~~~~~~~~Move 2~~~~~~~~~~~~~~~~
The_Rock = YourFighter('Dwayne "The Rock" Johnson', '49 y/o', '185cm', ["The People's Smolder", "The Thing He Was Cooking"])

To set the nickname for your object, input your object then serparate it by a period then the command for changing the nickname
~Object~~~Method~~~nickName~~
The_Rock.set_name("The Wock")

Adding a move to your fighter is simple. First input th object and seperate with a period, then use the command for adding the move.
~Object~~~Method~~~~~~~~addMove~~~~~~~~
The_Rock.add_move("The People's Elbow")

After these are the stating of the private variables and their print messages
~Print~Message~~~~~~~~~~~~~~~~~~~~Object~~~Method~~~~~~~~~~~~  
print("Your Fighter's name is",The_Rock.get_name())    
print("Your Fighter's age is",The_Rock.get_age())
print("Your Fighter's height is",The_Rock.get_height())   
print("Your Fighter's special moves are",The_Rock.get_moves())

Finally to use the moves that your fighter has, you must print the object and its name, then write the object and use the use_move method. Having nothing in the use_move method would use the randint function
to use a random move from their move set. Writing the specific move would that exactly , but inputting the wrong thing would make the fighter to use an 'Invalid Move'.
~print~~Object~~~method~~~~~print~~Object~~~Method~~~~
print(The_Rock.get_name(), 'used',The_Rock.use_move())

To run the main function, you must type python3 and the function name into windows terminal, this being class.py.





