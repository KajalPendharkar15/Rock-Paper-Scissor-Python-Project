#!/usr/bin/env python
# coding: utf-8

# # ROCK PAPER SCISSORS Python Project
# 

# In[1]:


print('Rock...')
print('Paper...')
print('Scissors...')


# In[5]:


player1 = input("Player 1, make your move:")
print("****NO CHEATING!\n\n" * 10)
player2 = input("Player 2, make your move:")


# In[9]:


if player1 == 'Rock' and player2 == 'Scissors':
    print("Player1 wins")
elif player1 == 'Rock' and player2 == 'paper':
      print("Player2 wins")
elif player1 == 'paper' and player2 == 'Rock': 
      print("Player1 wins")
elif player1 == 'paper' and player2 == 'Scissors': 
     print("Player2 wins")
elif player1 == 'Scissors' and player2 == 'Rock': 
    print("Player2 wins")
elif player1 == 'Scissors' and player2 == 'paper':
          print("Player1 wins")
elif player1 == player2:
    print('OOps its a tie...!')
else: 
    print('Something wennt wrong!')


# # NESTED IF....ELSE STATEMENT
# 

# In[10]:


if player1 == player2:
    print("Its a tie!")
elif player1 == 'Rock':
    if player2 == 'Scissors':
            print("Player1 wins")
    elif player2 == 'paper':
         print("Player2 wins")
elif player1 == 'paper':
        if player2 == 'Rock':
             print("Player1 wins")
        elif player2 == 'Scissors':
            print("Player2 wins")
elif player1 == 'Scissors':   
     if player2 == 'paper':
            print("Player1 wins")
     elif player2 == 'Rock':
        print("Player2 wins")
else: 
    print('Something wennt wrong!')
  
            

        
    


# In[ ]:




