#!/usr/bin/env python
# coding: utf-8

# In[1]:

### general thought: keep an eye out for any spacing issues like missing a space after a comma

from IPython.display import clear_output

def display_board(board):

    ### skipping index 0 isn't a good idea
    ### it's just a bit weird and you've got useless data in your array
    
    ### Unrelated but you don't really need to assign variables here since you're not reusing anything
    ### just go print(board[0:3]) or whatever
    
    ### In terms of structure, maybe board could be an array of arrays? 
    ### i.e. [[null, null, null], [null, null, null], [null, null, null]]
    ### (Complete tangent, maybe ignore this, but Python doesn't have null? I guess you could use None instead
    ### but I don't know how None is typically used in Python. Empty strings could be ok)
    ### That way display_board could just be:
    ### clear_output()
    ### for row in board:
    ###    print(row)
    ### or have some fancier function(s) that'll print it in a more board like fashion
    
    row1 = board[7::]
    row2 = board[4:7]
    row3 = board[1:4]
    
    clear_output()
    print(row1)
    print(row2)
    print(row3)


# In[2]:

### Naming things is always tough - not being sarcastic! But I'm not sure `player_input` really gets at what's going on here
### this is more like starting the game, or player choosing their symbol. specifically "input" feels too generic here
def player_input():
    
    ### choice may be too generic as well
    ### player_symbol or player_marker as the name would mean you need less context to read this and understand what the code is doing
    choice = "BLANK"
    acceptable_choice = ["X", "O"]
    players = {"p1": "", "p2": ""}
    
    ### the case of the x or the o doesn't really matter to the player or for the game
    ### I would probably pick a case and then make sure the comparison happens in that case
    ### e.g. while choice.upper() not in acceptable_choice
    while choice not in acceptable_choice:
    
        choice = input("Player 1, would you like to be X or O? ")
        
        ### if choice.upper() not in acceptable_choice
        if choice not in acceptable_choice:
            print("Sorry I dont understand, please enter X or O.")
        
        ### don't really need a second if here, could just be an else
        ### the choice will be good or not
        if choice in acceptable_choice:
            ### this can be simplified using a ternary operator
            ### players["p1"] = choice
            ### players["p2"] = "o" if choice == "x" else "x"
            if choice == "X":
                players["p1"] = "X"
                players["p2"] = "O"
            elif choice =="O":
                players["p1"] = "O"
                players["p2"] = "X"
                
                
    print(f"Player 1 you are {players['p1']} and Player 2 you are {players['p2']}. Player 1 you are first.")
    return (players)            


# In[3]:


def player_move(board,marker):
    
    def space_check(board, choice):
        ### this could probably just be a ternary as well
        ### return False if board[choice] else True
        ### I think empty strings are falsey in Python and other strings are not
        ### that means `if "string"` evaluates to True and `if ""` is False 
        if board[choice] == '':
            return True
        else:
            return False
    
    choice = "BLANK"
    acceptable_range = ["1","2","3","4","5","6","7","8","9"]
    ### check seems unnecessary here, you could just call the function in the if condition below without ever assigning to a variable
    check = False
    
    
    while choice not in acceptable_range:
        
        choice = input("Please select a position from 1 to 9: ")
        
        if choice not in acceptable_range:
            print("Sorry I did not understand. Please select a number from 1 to 9.")
            
        if choice in acceptable_range:
            choice = int(choice)
            check = space_check(board, choice)
            ### if space_check(board, choice)
            if check == True:
                choice = int(choice)
                break
          ### elif seems unnecessary here, an else would work fine
            elif check == False:
                print("Sorry that space is taken. Please select an available space.")


    ### this could probably be included in the if above
    ### board[int(choice)] = marker
    board[choice] = marker


# In[4]:


def game_win(board, marker):
    
    ### not sure the marker matters here, you just care if a symbol is in a line. not that a symbol is in a line and matches a symbol passed in
    ### also seems weird to have a bunch of ifs that all return the same thing. I might go with one ludicrously long if or or or but that's also kinda gross
    if board[7] == board[8] == board[9] == marker or board[1] == board[1] == board[2] == board[3] == marker or board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[5] == board[3] == marker or board[1] == board[5] == board[9] == marker:
        return True
    elif board[7] == board[4] == board[1] == marker or board[8] == board[5] == board[2] == marker or board[9] == board[6] == board[3] == marker:
        return True
    else:
        return False
    
    
    


# In[5]:


def game_tie(board, marker):
    
    list_check = []
    
          ### right here's an example of where skipping index 0 of the array gives you weird code
          ### you could just be going for i in board, but you can't trust what's in board[0].
    for i in board[1::]:
        
    
          ### I think you could just do `if i`
        if i != "":
            list_check.append(i)
          ### I'm not familiar enough with python, but is the pass necessary here? could just have an if without an else?
        else:
            pass
    
    return len(list_check) == 9
        


# In[6]:


def play_again():
    choice = "blank"
    
    while choice not in ["Y","N"]:
        
        choice =input("Play again? Please enter Y or N: ")
        
        if choice not in ["Y","N"]:
            print("Sorry I do not understand. Please select Y for yes or N for no.")
        
    if choice == "Y":
        return False
    else:
        print("See you next time!")
        return True
            


# In[7]:


board = ['','','','','','','','','','']
players = player_input()
marker1 = players["p1"]
marker2 = players["p2"]

game_off = False

while game_off == False:
    
    position1 = player_move(board,marker1)
    display_board(board)
    position2 = player_move(board,marker2)
    display_board(board)
    
    if game_win(board,marker1) == True:
        print("Player 1 has won the game!")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
    elif game_win(board,marker2) == True:
        print("Player 2 has won the game!")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
    elif game_tie(board,marker1) == True:
        print("Draw! How boring.")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
    ### else pass seems weird again
    ### I'd try turning the above elif into an else
    else:
        pass
    


# In[ ]:




