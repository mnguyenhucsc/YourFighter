#matthew nguyen hoang
#prof. hari 
#source: Nicholas Luong SJSU
#cse 20


#this is for the random move generator if the person decides to not dictate a move
import random

class YourFighter:
#this is the constructor 
    def __init__(self, name, age, height, moves):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__moves = moves
#the get/set functions  
#this get method should receive the name of the fighter
    def get_name(self):
        return(self.__name)
#this get method should receive the age of the fighter
    def get_age(self):
        return(self.__age)
#this get method should receive the height of the fighter   
    def get_height(self):
        return(self.__height)
#thhis should get the moves out of the list out of the main function
    def get_moves(self):
        move=''
#this goes through the list of moves
        for i in range(len(self.__moves)):
            if i == len(self.__moves) - 2:
#this adds the 'and' in the print statement
                move += self.__moves[i] + ' and '
            else:
#this adds a ' ' in the print statement
                move += self.__moves[i] + ' '
        return move
#this overwrites the name of the fighter giving them a nick name
    def set_name(self, nickName):
        self.__name = nickName

#the two other functions
#this method adds moves to the move set of the object
    def add_move(self,addMove):
#this appends the list of moves and takes the blank space for the new move
        self.__moves.append(addMove)
#this is the use move method
    def use_move(self,move=None):
#if the user does not input a specific move, then the fighter uses a random move using randint
        if move == None:
            return self.__moves[random.randint(0,len(self.__moves)-1)]
#if a specific move is stated, it is used.
        elif move in self.__moves:
            return move
#if a move is used that is not part of the list, it returns that it is an Invalid Move            
        else:
            return 'Invalid Move'
    

#this is the main function
def main():
#this is the object; its name, age, height, and move set
    The_Rock = YourFighter('Dwayne "The Rock" Johnson', '49 y/o', '185cm', ["The People's Smolder", "The Thing He Was Cooking"])
#this sets the nick name
    The_Rock.set_name("The Wock")
#this adds a move
    The_Rock.add_move("The People's Elbow")
#these here are the print messages for the get methods
    print("Your Fighter's name is",The_Rock.get_name())
    print("Your Fighter's age is",The_Rock.get_age())
    print("Your Fighter's height is",The_Rock.get_height())
    print("Your Fighter's special moves are",The_Rock.get_moves())
#this is where the object uses their move, either random or specific
    print(The_Rock.get_name(), 'used',The_Rock.use_move())

#this is the object; its name, age, height, and move set
    John_Cena = YourFighter ('John Cena', '44 y/o', '185cm',['The Five Knuckle Shuffle','Bing Chilling'])
#this sets the nick name    
    John_Cena.set_name('John Xina')
#these here are the print messages for the get methods
    print("Your Fighter's name is",John_Cena.get_name())
    print("Your Fighter's age is",John_Cena.get_age())
    print("Your Fighter's height is",John_Cena.get_height())
    print("Your Fighter's special moves are",John_Cena.get_moves())
#this is where the object uses their move, either random or specific
    print(John_Cena.get_name(), 'used',John_Cena.use_move())

if __name__ == "__main__":
    main()
