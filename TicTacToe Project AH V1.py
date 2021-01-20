#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    print(board[7::])
    print(board[4:7])
    print(board[1:4])


# In[2]:


def player_marker():
    
    marker = "BLANK"
    acceptable_choice = ["X", "O"]
    players = {"p1": "", "p2": ""}
    
    while marker.upper() not in acceptable_choice:
    
        marker = input("Player 1, would you like to be X or O? ").upper()
        
        if marker.upper() not in acceptable_choice:
            print("Sorry I dont understand, please enter X or O.")
        
        else:
            if marker.upper() == "X":
                players["p1"] = "X"
                players["p2"] = "O"
            elif marker.upper() =="O":
                players["p1"] = "O"
                players["p2"] = "X"
                
                
    print(f"Player 1 you are {players['p1']} and Player 2 you are {players['p2']}. Player 1 you are first.")
    return (players)                     


# In[3]:


def player_move(board,marker):
    
    def space_check(board, choice):
    
        return True if board[choice] == '' else False
    
    choice = "BLANK"
    acceptable_range = ["1","2","3","4","5","6","7","8","9"]
    
    
    while choice not in acceptable_range:
        
        choice = input("Please select a position from 1 to 9: ")
        
        if choice not in acceptable_range:
            print("Sorry I did not understand. Please select a number from 1 to 9.")
            
        else:
            choice = int(choice)
            if space_check(board, choice):
                choice = int(choice)
                break
            else:
                print("Sorry that space is taken. Please select an available space.")


    board[choice] = marker


# In[4]:


def game_win(board, marker):
    
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
    
    for i in board[1::]:
          if i != "":
            list_check.append(i)
    
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
players = player_marker()
marker1 = players["p1"]
marker2 = players["p2"]

game_off = False

while game_off == False:
    
    print("Player ONE your turn")
    player_move(board,marker1)
    display_board(board)
    
    if game_win(board,marker1) == True:
        print("Player 1 has won the game!")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
        else:
            break
    elif game_win(board,marker1) == True:
        print("Player 1 has won the game!")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
        else:
            break
    elif game_tie(board,marker1) == True:
        print("Draw! How boring.")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
        else:
            break
    
    print("Player TWO your turn.")
    player_move(board,marker2)
    display_board(board)
    
    if game_win(board,marker2) == True:
        print("Player 2 has won the game!")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
        else:
            break
    elif game_win(board,marker2) == True:
        print("Player 2 has won the game!")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
        else:
            break
    elif game_tie(board,marker2) == True:
        print("Draw! How boring.")
        game_off = play_again()
        if game_off == False:
            board = ['','','','','','','','','','']
        else:
            break
    


# In[ ]:




