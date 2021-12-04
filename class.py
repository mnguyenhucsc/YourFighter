#matthew nguyen hoang
#prof. hari 
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

    def get_moves(self):
        move=''
        for i in range(len(self.__moves)):
            if i == len(self.__moves) - 2:
                move += self.__moves[i] + ' and '
            else:
                move += self.__moves[i] + ' '
        return move

    def set_name(self, nickName):
        self.__name = nickName

#the two other functions
    def add_move(self,addMove):
        self.__moves.append(addMove)

    def use_move(self,move=None):
        if move == None:
            return self.__moves[random.randint(0,len(self.__moves)-1)]
        elif move in self.__moves:
            return move
        else:
            return 'Invalid Move'
    


def main():
    The_Rock = YourFighter('Dwayne "The Rock" Johnson', '49 y/o', '185cm', ["The People's Smolder", "The Thing He Was Cooking"])
    The_Rock.set_name("The Wock")
    The_Rock.add_move("The People's Elbow")
    
    print("Your Fighter's name is",The_Rock.get_name())
    print("Your Fighter's age is",The_Rock.get_age())
    print("Your Fighter's height is",The_Rock.get_height())
    print("Your Fighter's special moves are",The_Rock.get_moves())
    print(The_Rock.get_name(), 'used',The_Rock.use_move())
    
    John_Cena = YourFighter ('John Cena', '44 y/o', '185cm',['The Five Knuckle Shuffle','Bing Chilling'])
    John_Cena.set_name('John Xina')
    print("Your Fighter's name is",John_Cena.get_name())
    print("Your Fighter's age is",John_Cena.get_age())
    print("Your Fighter's height is",John_Cena.get_height())
    print("Your Fighter's special moves are",John_Cena.get_moves())
    print(John_Cena.get_name(), 'used',John_Cena.use_move())

if __name__ == "__main__":
    main()