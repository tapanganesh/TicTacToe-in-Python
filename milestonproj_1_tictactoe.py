#!/usr/bin/env python
# coding: utf-8

# In[82]:


from IPython.display import clear_output

def displayboard(board):
    pos=0
    print()
    for i in range(0,3):
        for h in range(0,3):
            for x in range(0,3):
                if x!=1:
                    print(" ",end="")
                elif x==1:
                    print(board[pos],end="")
            if h!=2:
                print("|",end="")
            pos=pos+1
        print()
        if i!=2:
            for d in range(0,12):
                print("-",end="")
        print()
        
    


# In[83]:


def getchoice():
    valid=False
    while valid==False:
        pos=input("Enter the position you want to choose:")
        if pos.isdigit():
            pos=int(pos)
            if pos<=9 and pos>=0:
                if board[pos-1]==str(pos) and board[pos-1]!="X" and board[pos-1]!="O":
                    valid=True
                else:
                    print("please choose a valid position:")
                    valid=False
            else:
                #clear_output()
                print("please choose a valid position:")
                valid=False
        else:
           # clear_output()
            print("please choose a valid position:")
            valid=False
    return pos
            


# In[84]:


def gameover():
    for i in range(0,9,3):
        global G,w
        if board[i]==board[i+1] and board[i+1]==board[i+2]:
            if board[i]=="X":
                w=2
            else:
                w=1
            G=1
            return True
    for i in range(0,3):
        if board[i]==board[i+3] and board[i+3]==board[i+6]:
            if board[i]=="X":
                w=2
            else:
                w=1
            G=1
            return True
    if (board[0]==board[4] and board[4]==board[8]):
            G=1
            if board[0]=="X":
                w=2
            else:
                w=1
            return True
    if(board[2]==board[4] and board[4]==board[6]):
            G=1
            if board[2]=="X":
                w=2
            else:
                w=1
        
            return True
    for c in board:
        if c.isdigit():
            return False
    G=0  
    return True


# In[85]:


def makeboard(board):
    board=["1","2","3","4","5","6","7","8","9"]


# In[91]:


gameend=False
i=2
G=2
w=0
board=["1","2","3","4","5","6","7","8","9"]
while gameend!=True:
#clear_output()
    print("PLAYER 1-O PLAYER 2-X")
    pos=getchoice()
    if i%2==0:
        board[pos-1]="O"
    else:
        board[pos-1]="X"
    displayboard(board)
    gameend=gameover()
    clear_output()
    if gameend==True:
       # print(f"g={G}")
        if G==1:
            print("GAME OVER")
            print(f"PLAYER {w} WINS!")
        elif G==0:
            print("GAME DRAW")
    i=i+1
    displayboard(board)
        
        
    


# In[ ]:




