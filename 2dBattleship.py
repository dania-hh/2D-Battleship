import os
from random import randint
import time
dim=10
starting_coordinates=[]
win=False

class Board:
	def __init__(self,dim,ships,turn):
		global starting_coordinates
		self.dim=dim
		self.numPlayers = 2
		self.turn = turn
		self.players=['USER', 'COMPUTER']
		self.board=[]
		self.ships=ships
		self.all_coordinates=[]
		self.store=[]
		self.mark=''
		

		#create board
		for row in range(self.dim):
			tempList=[]
			for col in range(self.dim):
				tempList.append(' ')
			self.board.append(tempList)
	
		for i in self.ships:
			done=False
			while done==False:

				#choosing a location on the board
				randomRow=randint(0,self.dim-1)
				randomCol=randint(0,self.dim-1)
				if self.board[randomRow][randomCol]==' ':

					#choosing randomly horz or vert
					layout=['h','v']
					randomLayoutIndex=randint(0,1)
					randomLayoutChoice=layout[randomLayoutIndex]

					#if horizontal
					if randomLayoutChoice=='h':

						#RIGHT
						length=0
						for box in range(i):
							if randomCol<=i:
								if self.board[randomRow][randomCol+box]==' ':
									length+=1
						if length==i:			
							for box in range(i):
								self.board[randomRow][randomCol+box]='*'
								self.all_coordinates.append(randomCol+box)
							done=True

							#LEFT	
							length=0
							if randomCol>=i-1:
								if self.board[randomRow][randomCol-box]==' ':
									length+=1
							if length==i:
								for box in range(i):
									self.board[randomRow][randomCol-box]='*'
									self.all_coordinates.append(randomCol-box)
								done=True

								
					#if vertical
					if randomLayoutChoice=='v':
						#UP
						length=0
						for box in range(i):
							if randomRow<=i:
								if self.board[randomRow+box][randomCol]==' ':
									length+=1
						if length==i:			
							for box in range(i):
								self.board[randomRow+box][randomCol]='*'
								self.all_coordinates.append(randomRow+box)
							done=True
							

							#DOWN	
							length=0
							if randomCol>=i-1:
								if self.board[randomRow-box][randomCol]==' ':
									length+=1
							if length==i:
								for box in range(i):
									self.board[randomRow-box][randomCol]='*'
									self.all_coordinates.append(randomRow-box)
								done=True
								
					#appending coordintes to coordinate list, will be used for ship info section			
					if done==True:
						starting_coordinates.append(randomRow+1)
						starting_coordinates.append(randomCol+1)
						


	#printing the board
	def printing(self,whoboard):
		self.whoboard=whoboard
		print('\n   ',whoboard,'\n')
		for cols in range(1,2):
			print ('     '+str(cols), end='')
		for cols in range(2,self.dim+1):
			print ('   '+str(cols), end='')
		print("\n    "+'----'*self.dim)
		for row in range(1,self.dim+1):
			if row<10:
				print(str(row),' |', end='')
			if row>=10:
				print(str(row),'|', end='')
			#rowList=[]
			for col in range(1,self.dim+1):
				print(self.board[row-1][col-1], end='  |')
			print()
			print('   ','----'*self.dim)
		print()

	def computer_attack(self):
		time.sleep(2)
		x=randint(0,self.dim-1)
		y=randint(0,self.dim-1)
		if self.board!='X' or self.board!='O':
			if self.board[x][y]=='*':
				self.board[x][y]='X'
				print('\nComputer successfully attacked.')
			else:
				self.board[x][y]='O'
				print('\nComputer missed target.')
			time.sleep(2)

		


	def winCheck(self):
		count=0
		for i in self.all_coordinates[0:6]:
			if self.board[self.all_coordinates[i+1]][self.all_coordinates[i+1]]=='X':
				count+=1
		if count==5:
			print('Your Aircraft Carrier has sunk')
		count=0	
		for i in self.all_coordinates[6:11]:
			if self.board[self.all_coordinates[i]][self.all_coordinates[i+1]]=='X':
				count+=1
		if count==4:
			print('Your Battleship has sunk')
		count=0
		for i in self.all_coordinates[11:14]:
			if self.board[self.all_coordinates[i]][self.all_coordinates[i+1]]=='X':
				count+=1
		if count==3:
			print('Your Submarine has sunk')
		count=0
		for i in self.all_coordinates[14:17]:
			if self.board[self.all_coordinates[i]][self.all_coordinates[i+1]]=='X':
				count+=1
		if count==3:
			print('Your Destroyer has sunk')
		count=0
		for i in self.all_coordinates[17:19]:
			if self.board[self.all_coordinates[i]][self.all_coordinates[i+1]]=='X':
				count+=1
		if count==2:
			print('Your Patrol Boat has sunk')
		count=0
		for i in self.all_coordinates[0:19]:
			if self.board[self.all_coordinates[i]][self.all_coordinates[i+1]]=='X':
				count+=1
		if count==18:
			print('All your ships have sunk!\nThe enemy has won.')
			win=True

		count=0
		for r in range(self.dim):
			for c in range(self.dim):
				if self.board[r][c]!='*':
					count+=1
		if count==0:
			print("You won!\nAll enemy ships have sunk.")
			win=True

#subclass for enemy board with hidden ships created
class Enemy(Board):
	def __init__(self,dim,ships,turn):
		Board.__init__(self,dim,ships,turn)
		for r in range(self.dim):
			for c in range(self.dim):
				if self.board[r][c]=='*':
					self.store.append(r)
					self.store.append(c)
					self.board[r][c]=' '
					self.score=0

	def user_attack(self):
		hit=True	
		x=int(attack[0])
		y=int(attack[1])
		
		while hit==True:
			self.mark=''
			
			for i in range(0,len(self.store),2):
				if x==self.store[i] and y==self.store[i+1]:
					self.mark='X'
					if self.mark=='X':
						self.board[x-1][y-1]='X'
						print('\nAttack Successful.')
						time.sleep(2)
						hit=False
				elif hit==True:
					self.mark='O'
					if self.mark=='O':
						self.board[x-1][y-1]='O'
						print('\nYou missed your target.')
						time.sleep(2)
						hit=False


turn=0
players=['USER','COMPUTER']

#creating board objects
user_BattleShip_Board=Board(10,[5,4,3,3,2],turn)
enemy_BattleShip_Board=Enemy(10,[5,4,3,3,2],turn)
print(user_BattleShip_Board.printing('My Ships'),enemy_BattleShip_Board.printing('Enemy Ships'),sep='\t',end='\t')
print()


#informing of whos turn
print(players[turn],"'s turn")

#providing user with information to clarify ship placement on board
shipInfo=print('\nInformation:\n\n |     Ship type    |   Length  | (r,c) Starting Co-ordinates\n','___'*20,'\n | Aircraft Carrier | 5 spaces  |','({0},{1})'.format(starting_coordinates[0],starting_coordinates[1]),'\n |    Battleship    | 4 spaces  |','({0},{1})'.format(starting_coordinates[2],starting_coordinates[3]),'\n |     Submarine    | 3 spaces  |','({0},{1})'.format(starting_coordinates[4],starting_coordinates[5]),'\n |     Destroyer    | 3 spaces  |','({0},{1})'.format(starting_coordinates[6],starting_coordinates[7]),'\n |    Patrol Boat   | 2 spaces  |','({0},{1})'.format(starting_coordinates[8],starting_coordinates[9]),'\n')


#trial=0
while win==False: 

	while players[turn]=='USER':
		attack=input('\nWhere will you aim?\nEnter input in the form: r,c ') 
		while len(attack.split(",")) != 2 or not attack.split(",")[0].isdigit() or not attack.split(",")[1].isdigit() or not (int(attack.split(",")[0]) in range(dim+1)) or not (int(attack.split(",")[1]) in range(dim+1)):
			print('Invalid input')
			attack=input('Which location (r,c) will you aim? ') 
		#trial+=1
		#trial=print('Trial #',trial)
		attack=attack.split(',')
		enemy_BattleShip_Board.user_attack()
		user_BattleShip_Board.winCheck()
		os.system('clear')
		user_BattleShip_Board.printing('My Ships')
		enemy_BattleShip_Board.printing('Enemy Ships')
		shipInfo=print('\nInformation:\n\n |     Ship type    |   Length  | (r,c) Starting Co-ordinates\n','___'*20,'\n | Aircraft Carrier | 5 spaces  |','({0},{1})'.format(starting_coordinates[0],starting_coordinates[1]),'\n |    Battleship    | 4 spaces  |','({0},{1})'.format(starting_coordinates[2],starting_coordinates[3]),'\n |     Submarine    | 3 spaces  |','({0},{1})'.format(starting_coordinates[4],starting_coordinates[5]),'\n |     Destroyer    | 3 spaces  |','({0},{1})'.format(starting_coordinates[6],starting_coordinates[7]),'\n |    Patrol Boat   | 2 spaces  |','({0},{1})'.format(starting_coordinates[8],starting_coordinates[9]),'\n')
		turn=(turn+1)%2
		print('   ',players[turn],"'s turn")


	while players[turn]=='COMPUTER':
		user_BattleShip_Board.computer_attack()
		user_BattleShip_Board.winCheck()
		os.system('clear')
		user_BattleShip_Board.printing('My Ships')
		enemy_BattleShip_Board.printing('Enemy Ships')
		shipInfo=print('\nInformation:\n\n |     Ship type    |   Length  | (r,c) Starting Co-ordinates\n','___'*20,'\n | Aircraft Carrier | 5 spaces  |','({0},{1})'.format(starting_coordinates[0],starting_coordinates[1]),'\n |    Battleship    | 4 spaces  |','({0},{1})'.format(starting_coordinates[2],starting_coordinates[3]),'\n |     Submarine    | 3 spaces  |','({0},{1})'.format(starting_coordinates[4],starting_coordinates[5]),'\n |     Destroyer    | 3 spaces  |','({0},{1})'.format(starting_coordinates[6],starting_coordinates[7]),'\n |    Patrol Boat   | 2 spaces  |','({0},{1})'.format(starting_coordinates[8],starting_coordinates[9]),'\n')
		turn=(turn+1)%2
		print('   ',players[turn],"'s turn")