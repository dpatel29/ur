import random
def dice():
	return random.randint(0,1)+random.randint(0,1)+random.randint(0,1)+random.randint(0,1)
whitepiece=[0,0,0,0,0,0,0]
blackpiece=[0,0,0,0,0,0,0]
white=0
black=0
skip=0
print("Welcome to Mocha's Ur Simulator!")
while white<7>black:
	#white's move
	if skip==0:
		roll=dice()
		print("WHITE TO ROLL:",white,"-",black,"\nWhite rolls a",roll)
		if roll!=0:
			playablepiece=[]
			#finding which pieces can be moved
			for i in range(len(whitepiece)):
				if whitepiece[i]+roll not in whitepiece:#can't step on another of your own pieces
					if not ((whitepiece[i]+roll==8) and (8 in blackpiece)):#can't step on opponent, but only on central lotus
						if whitepiece[i]+roll<=15:#can't overgo
							playablepiece+=[i]
			if playablepiece!=[]:
				print("Choose a piece to play:",playablepiece)
				print("Keep in mind, the positions of your pieces are:",whitepiece)
				print("Keep in mind, the positions of black are:",blackpiece)
				choice=-1
				while choice not in playablepiece:
					try:
						choice=int(input("> "))
					except ValueError:
						choice=random.choice(playablepiece)#I gave you the fucking chance and you lost it
				whitepiece[choice]+=roll
				#capture
				if (13>whitepiece[choice]>4) and (whitepiece[choice] in blackpiece):
					for i in range(len(blackpiece)):
						if blackpiece[i]==whitepiece[choice]:
							blackpiece[i]=0
				#lotus reroll
				if whitepiece[choice]==4 or whitepiece[choice]==8 or whitepiece[choice]==14:skip=1
				#cross the end
				elif whitepiece[choice]==15:
					white+=1
					del whitepiece[choice]
				#print
				try:
					print("White has moved from",whitepiece[choice]-roll,"to",whitepiece[choice],".")
				except IndexError:
					pass
			else:print("You can't move!")
		else:print("You rolled a zero!")
	else:skip-=1
	#black's move, mirror of white's
	if skip==0:
		roll=dice()
		print("BLACK TO ROLL:",white,"-",black,"\nBlack rolls a",roll)
		if roll!=0:
			playablepiece=[]
			for i in range(len(blackpiece)):
				if blackpiece[i]+roll not in blackpiece:
					if not ((blackpiece[i]+roll==8) and (8 in whitepiece)):
						if blackpiece[i]+roll<=15:
							playablepiece+=[i]
			if playablepiece!=[]:
				print("Choose a piece to play:",playablepiece)
				print("Keep in mind, the positions of your pieces are:",blackpiece)
				print("Keep in mind, the positions of white are:",whitepiece)
				choice=-1
				while choice not in playablepiece:
					try:
						choice=int(input("> "))
					except ValueError:
						choice=random.choice(playablepiece)
				blackpiece[choice]+=roll
				if (13>blackpiece[choice]>4) and (blackpiece[choice] in whitepiece):
					for i in range(len(whitepiece)):
						if whitepiece[i]==blackpiece[choice]:
							whitepiece[i]=0
				if blackpiece[choice]==4 or blackpiece[choice]==8 or blackpiece[choice]==14:skip=1
				elif blackpiece[choice]==15:
					black+=1
					del blackpiece[choice]
				try:
					print("Black has moved from",blackpiece[choice]-roll,"to",blackpiece[choice],".")
				except IndexError:
					pass
			else:print("You can't move!")
		else:print("You rolled a zero!")
	else:skip-=1
if white==7:print("White wins!")
else:print("Black wins!")
print(white,"-",black)