import sys
import pygame
import time
import os
from random import *
from pygame.locals import *
from win32api import GetSystemMetrics

def crFgr(row,col,boardGrid,screen,y):#Draws rectangles used in created shape
	screen.lock()#restricts display data from being changed at all and stores it for it to be accessed by other functions
	for i in range(row):							
		for u in range(col):						
			if boardGrid[i][u]==1 or boardGrid[i][u]==2:	
				pygame.draw.rect(screen, (0,(choice(range(170,204))),0), Rect((u*y,i*y+y), (y-2,y-2)))#Draws rectangle using a random shade of green
	pygame.display.update()#updates display
	screen.unlock()
def rowpos_limit(rowpos,row,col,boardGrid): # defines rows in the grid that objects can be without causing game to end
	if rowpos==row-1: 
		return True
	for i in range(row):
		for u in range(col):
			if boardGrid[i][u]==2:
				if i<row-2:
					if boardGrid[i+1][u]==1:
					   return True
				else:
				    return True
				    
#Blocks and their potential position confgrurations
def fgr1(lft,rght,colpos,rowpos,p,row,col,boardGrid):# Uses mv_fgr function to define block in a specific position and place in gridspace(boardGrid)
	if p==1:   mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid)#t shape	
	if p==2: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid)
	if p==3: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid)		
	if p==4: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid)	
def fgr2(lft,rght,colpos,rowpos,p,row,col,boardGrid):
	if p==1:   mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid),mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid),mv_fgr(lft,rght,colpos-1,rowpos+1,row,col,boardGrid)#L shape
	if p==2: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid),mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid)	
	if p==3: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid),mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid),mv_fgr(lft,rght,colpos-1,rowpos+1,row,col,boardGrid)		
	if p==4: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid),mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid)
def fgr3(lft,rght,colpos,rowpos,p,row,col,boardGrid):
	if p==1:   mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos+1,row,col,boardGrid)#J shape
	if p==2: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos-1,row,col,boardGrid)	 
	if p==3: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos-1,row,col,boardGrid)	
	if p==4: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos+1,row,col,boardGrid)	
def fgr4(lft,rght,colpos,rowpos,p,row,col,boardGrid):
	if p==1:   mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos+1,row,col,boardGrid)#S shape
	if p==2: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos+1,row,col,boardGrid)	
	if p==3: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos-1,row,col,boardGrid)	 
	if p==4: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos-1,row,col,boardGrid)
def fgr5(lft,rght,colpos,rowpos,p,row,col,boardGrid):
	if p==1:   mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos+1,row,col,boardGrid)#Z shape
	if p==2: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos-1,row,col,boardGrid)	
	if p==3: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos-1,row,col,boardGrid)	
	if p==4: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos+1,row,col,boardGrid)
def fgr6(lft,rght,colpos,rowpos,p,row,col,boardGrid):
	if p==1:   mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid)#I shape
	if p==2: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid)
	if p==3: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos+1,row,col,boardGrid)	
	if p==4: mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos-1,rowpos,row,col,boardGrid)
def fgr7(lft,rght,colpos,rowpos,p,row,col,boardGrid):
	mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid), mv_fgr(lft,rght,colpos,rowpos-1,row,col,boardGrid), mv_fgr(lft,rght,colpos+1,rowpos-1,row,col,boardGrid),mv_fgr(lft,rght,colpos+1,rowpos,row,col,boardGrid) # Square	
def colpos_limit(row,col,boardGrid):# defines columns in the grid that objects can go to
	for i in range(row):
		for u in range(col):
			if boardGrid[i][u]==2 and boardGrid[i][u-1]==1: # if block is present and the gridspace to left is not available, it returns 1
				return 1
			if boardGrid[i][u]==2 and boardGrid[i][u+1]==1:#if block is present and the gridspace to the right is not available, returns 2
				return 2
			elif  boardGrid[i][0]==2:#if block next to left boundary, it returns 1
				return 1
			elif  boardGrid[i][col-1]==2:#if block next to right boundary, it returns 2
				return 2
def mv_fgr(lft,rght,colpos,rowpos,row,col,boardGrid):  #defines where a block currently is in column position and how it moves depending on left and right variables
	colpos=colpos+lft+rght
	if lft+rght==0:
	    boardGrid[rowpos][colpos]=2
	elif lft+rght==1:
	    boardGrid[rowpos][colpos-1]=2
	elif lft+rght==-1:
	    boardGrid[rowpos][colpos+1]=2
	return
def rot8(i,u,row,col,boardGrid): # defines whether block can rotate
	if i<col-1:
		if boardGrid[u][i+1]!=1:
		    if boardGrid[u][i-1]!=1 and boardGrid[u-1][i-1]!=1 and boardGrid[u-1][i]!=1 and boardGrid[u-1][i+1]!=1 and boardGrid[u+1][i-1]!=1 and boardGrid[u+1][i]!=1 and boardGrid[u+1][i+1]!=1:
                        return True
                    else:
			return False
		if boardGrid[u][i-1]!=1:
                    if boardGrid[u][i-1]!=1 and boardGrid[u-1][i-1]!=1 and boardGrid[u-1][i]!=1 and boardGrid[u-1][i+1]!=1 and boardGrid[u+1][i-1]!=1 and boardGrid[u+1][i]!=1 and boardGrid[u+1][i+1]!=1:
                        return True
                    else:
                        return False
	else:
		return False

def pstion_limit(p):#restricts the amount of positions to the 4 defined
	if p>4:
		p=1 
		return p
	elif p<1:
		p=4
		return p
	else:
		return p
		

def attach_fgr_to_body(loop,row,col,boardGrid):	#places rectangles 
	if loop==False:				
		for i in range(row):
			for u in range(col):
				if boardGrid[i][u]==2:
				    boardGrid[i][u]=1
def traceReplace(row,col,boardGrid):		# Makes grid positions previously taken over by rectangle blank/0 again			
	for r in range(row):
		for c in range(col):
			if boardGrid[r][c]==2:
			    boardGrid[r][c]=0
def get_fgr(lft,rght,colpos,rowpos,pos,fgr,row,col,boardGrid): #assigns figure to integer in loop
	if fgr==1: fgr1(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
	if fgr==2: fgr2(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
	if fgr==3: fgr3(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
	if fgr==4: fgr4(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
	if fgr==5: fgr5(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
	if fgr==6: fgr6(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
	if fgr==7: fgr7(lft,rght,colpos,rowpos,pos,row,col,boardGrid)
def lineRplace(row,col,boardGrid):#Replaces boardGrid with 0s/blanks again if it is full
    for i in range(row):
		a=0
		for u in range(col):
			if boardGrid[i][u]!=0 and boardGrid[i][u]!=2:
			    a=a+boardGrid[i][u]
			    if a==col:
			        del boardGrid[i]
			        zero=[0 for s in range(col)]
			        boardGrid.insert(0,zero)
			        return True	        
def GameMain():
    #Initialization and Variables Block
    if GetSystemMetrics(1)>=720: y=30 #Sets y variable according to screen size, y variable is used later to determine size of game window
    else:y=10
    row = int(GetSystemMetrics(1)/50) #sets row count according to screen size
    col = int(GetSystemMetrics(0)/120) #sets column count according to screen size
    boardGrid = [[ 0 for i in range(col)] for u in range(row)] # Creates a list of lists that can be used to represent a grid [[0 * columns] * rows] where 0 is a placeholder
    pygame.init() # initializes pygame 
    screen=pygame.display.set_mode((col*y,row*y),0,16) #sets visiblity of game grid based on columns and rows times y variable
    pygame.display.set_caption('Tetris') # Defines name
    background = pygame.Surface(screen.get_size()) # defines background of game window's size
    background.fill((0,0,0)) #background color
    font = pygame.font.Font(None, 24) #font of text displayed
    text = font.render("Press Escape or Q to Quit", 1, (255, 255, 255)) #Defines text and color of text
    textpos = text.get_rect() # sets where text can be
    textpos.centerx = background.get_rect().centerx # sets text box location
    background.blit(text, textpos) #sets text on top of background
    spd=2.5
    rght=0
    lft=0
    score=0
    while True:
        #Main Game Loop
        rowpos=0 # spawn row
   	colpos=col/2 # spawn col
   	spd_up=1   # gravity
   	loop=True		
   	fgr=randint(1,7) # random integer to spawn figure	
   	pstion=randint(0,4)#Possible Positions
   	while loop == True:
            rowpos=rowpos+1 #Gravity
            colpos_limit(row,col,boardGrid)
            for z in range(10):#Higher the number, higher
                screen.unlock()
                screen.blit(background,(0,0))
                screen.lock()
                for event in pygame.event.get():#detects events
                    screen.unlock()
                    screen.blit(background,(0,0)) 
                    screen.lock()
                    if event.type==QUIT:#if you press the Red X it displays your score then exits
                        print "Your score was",int(score)
                        print "Goodbye"
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:#Controls
                        if event.key==K_ESCAPE or event.key==K_q:
                            print "Your score was",int(score)
                            print "Goodbye"
                            pygame.quit()
                            sys.exit()
                        if event.key==K_w or event.key==K_UP:#If you press w, calls rotate function/causes position to change
                            if rot8(colpos,rowpos,row,col,boardGrid)==True:
                                pstion=pstion+1
                        if event.key==K_a or event.key==K_LEFT:#if you press a or the left arrow key, it makes the left variable -1 moving the column position of figure left one on the grid
                            lft=-1					
                        if event.key==K_d or event.key==K_RIGHT:#if you press d or the right arrow key, it makes the right variable 1 moving the column position of figure right one on the grid
                            rght=1
                        if event.key==K_s or event.key == K_DOWN:# if you press down arrow or s key, makes speed up variable equal to y(set by screen size) divided by default speed
                            if spd_up == 1:
                                spd_up = y/spd
                            else:
                                spd_up = 1
                if colpos_limit(row,col,boardGrid)==1:#if you are along left boundary or to the left of your block is a stable block(1), you cannot move to the left
                    lft=0
                if colpos_limit(row,col,boardGrid)==2:#if you are along right boundary or to the right of your block is a stable block(1), you cannot move right
                    rght=0
                time.sleep(0.075/spd/spd_up)# delays updating by predetermined variable divided by speed and speed up
                pstion=pstion_limit(pstion)# makes sure position returns to 1 if position 4 is rotated off of
                traceReplace(row,col,boardGrid)#removes displaying blocks but not variables
                get_fgr(lft,rght,colpos,rowpos,pstion,fgr,row,col,boardGrid)#defines where block can move and where it currently should be depending on figure selected
                colpos=colpos+lft+rght#changes position left and right
                lft=rght=0#restricts left and right to only moving once
                crFgr(row,col,boardGrid,screen,y)#Draws new shape based off variables given from get_fgr and input given
            if rowpos_limit(rowpos,row,col,boardGrid)==True:#checks if block has met another block or boundary
                loop=False
            attach_fgr_to_body(loop,row,col,boardGrid)#makes block a stable/unmovable block if rowpos_limit(rowpos) has bee fufilled
            lineRplace(row,col,boardGrid)#Clears line if full line created
            score=score+0.2#Score based on time alive
        if rowpos==1:#If there is a stable/unmovable block at spawn, ends game
   	    print "Your score was",int(score)
   	    print "YOU LOST"
   	    pygame.quit()
   	    sys.exit()
GameMain()