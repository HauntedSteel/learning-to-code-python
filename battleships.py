import time
import random

board1 = {"A":[0,0,0,0,0,0,0,0,0,0],
         "B":[0,0,0,0,0,0,0,0,0,0],
         "C":[0,0,0,0,0,0,0,0,0,0],
         "D":[0,0,0,0,0,0,0,0,0,0],
         "E":[0,0,0,0,0,0,0,0,0,0],
         "F":[0,0,0,0,0,0,0,0,0,0],
         "G":[0,0,0,0,0,0,0,0,0,0],
         "H":[0,0,0,0,0,0,0,0,0,0],
         "I":[0,0,0,0,0,0,0,0,0,0],
         "J":[0,0,0,0,0,0,0,0,0,0]}
board2 = {"A":[0,0,0,0,0,0,0,0,0,0],
         "B":[0,0,0,0,0,0,0,0,0,0],
         "C":[0,0,0,0,0,0,0,0,0,0],
         "D":[0,0,0,0,0,0,0,0,0,0],
         "E":[0,0,0,0,0,0,0,0,0,0],
         "F":[0,0,0,0,0,0,0,0,0,0],
         "G":[0,0,0,0,0,0,0,0,0,0],
         "H":[0,0,0,0,0,0,0,0,0,0],
         "I":[0,0,0,0,0,0,0,0,0,0],
         "J":[0,0,0,0,0,0,0,0,0,0]}

abclist = ["A","B","C","D","E","F","G","H","I","J"]
positions1 = list(board1.values())
positions2 = list(board2.values())
boards = [board1,board2]

#BOARD IDS:
#0 is empty
#1 is miss
#2 is hit3ship
#4 is hit4ship
#6 is hit5ship
#8 is hit2ship
#3 is 3ship
#5 is 4ship
#7 is 5ship
#9 is 2ship

def generate(boards, size, times, ID):
  generated = 0
  for boardnum in range(2): #generate for both boards

    generated = 0
    while generated < times: #generate 2 ships
      
      #var for checking if space is free for ship placement
      checkvalid = 1 
      
      #randomize vertical/horizontal placement of ship
      verhorroll = random.randint(1,2)
      
      if verhorroll == 1: #horizontal placement
        #generates a position
        positionroll = random.randint(0,10-size) 
        abcpositionroll = random.randint(0,9)
  
        #checks if space is free for ship placement
        for counter in range(size): 
          if boards[boardnum][abclist[abcpositionroll]][positionroll + counter]== 3 or boards[boardnum][abclist[abcpositionroll]][positionroll+counter]== 5 or boards[boardnum][abclist[abcpositionroll]][positionroll+counter]== 7 or boards[boardnum][abclist[abcpositionroll]][positionroll+counter]== 9:
            checkvalid = 0
            break
            
        #restart loop if not free
        if checkvalid == 0:
          continue
          
        else: 
          generated += 1 
          #places ship
          for counter in range(size):
            boards[boardnum][abclist[abcpositionroll]][positionroll+counter] = ID
  
      else: #vertical placement
        #generates new position
        abcpositionroll = random.randint(0,10-size)
        positionroll = random.randint(0,9)
  
        #checks if space is free for placement
        for counter in range(size):
          if boards[boardnum][abclist[abcpositionroll+counter]][positionroll]== 3 or boards[boardnum][abclist[abcpositionroll+counter]][positionroll]== 5 or boards[boardnum][abclist[abcpositionroll+counter]][positionroll]== 7 or boards[boardnum][abclist[abcpositionroll+counter]][positionroll]== 9:
            checkvalid = 0
            break
  
        #restart loop if not free
        if checkvalid == 0:
          continue
        else: 
          generated += 1
          #places ship
          for counter in range(size):
            boards[boardnum][abclist[abcpositionroll+counter]][positionroll] = ID
  return boards


def drawboards(abclist,positions1,positions2):
  print("Your board: ")
  print()
  print("    0  1  2  3  4  5  6  7  8  9")
  print()
  adder = 0
  for counter in positions1:
    print(abclist[adder],end=" ")
    adder += 1
    for iteration in counter:
      if iteration == 0:
        print("  ?",end="")
      if iteration == 1:
        print("   ",end="")
      if iteration == 2 or iteration == 4 or iteration == 6 or iteration == 8:
        print("  @",end="")
      #separate ship prints (edit for debugging/seeing ship generation) 
      if iteration == 3:
        print("  ?",end="")
      if iteration == 5:
        print("  ?",end="")
      if iteration == 7:
        print("  ?",end="")
      if iteration == 9:
        print("  ?",end="")
    print()
  print()
  print()
  print("Enemy board: ")
  print()
  print("    0  1  2  3  4  5  6  7  8  9")
  print()
  adder = 0
  for counter in positions2:
    print(abclist[adder],end=" ")
    adder += 1
    for iteration in counter:
      if iteration == 0:
        print("  ?",end="")
      if iteration == 1:
        print("   ",end="")
      if iteration == 2 or iteration == 4 or iteration == 6 or iteration == 8:
        print("  @",end="")
       #separate ship printing (edit for debugging/seeing ship generation) 
      if iteration == 3:
        print("  ?",end="")
      if iteration == 5:
        print("  ?",end="")
      if iteration == 7:
        print("  ?",end="")
      if iteration == 9:
        print("  ?",end="")
    print()
  print()

def tuple_convert(string):
  newtup = (string[0].upper(),int(string[1]))
  return newtup

  #checks if a ship has been sunken - i've honestly forgotten how this works
def checkships(board, shipsunken):
  values = list(board.values())
  shiplist = []
  consec = False
  for counter in values:
    for num in counter:
      if num == 2:
        if consec:
          shiplist[-1].append(num)
        else:
          shiplist.append([num])
        consec = True
      else:
        consec = False
  #vertical check
  consec = False
  for counter in range(9):
    for num in values:
      if num[counter] == 2:
        if consec:
          shiplist[-1].append(num[counter])
        else:
          shiplist.append([num[counter]])
        consec = True
      else:
        consec = False
  consec = False
  for counter in values:
    for num in counter:
      if num == 4:
        if consec:
          shiplist[-1].append(num)
        else:
          shiplist.append([num])
        consec = True
      else:
        consec = False
  consec = False
  for counter in range(9):
    for num in values:
      if num[counter] == 4:
        if consec:
          shiplist[-1].append(num[counter])
        else:
          shiplist.append([num[counter]])
        consec = True
      else:
        consec = False
  consec = False
  for counter in values:
    for num in counter:
      if num == 6:
        if consec:
          shiplist[-1].append(num)
        else:
          shiplist.append([num])
        consec = True
      else:
        consec = False
  consec = False
  for counter in range(9):
    for num in values:
      if num[counter] == 6:
        if consec:
          shiplist[-1].append(num[counter])
        else:
          shiplist.append([num[counter]])
        consec = True
      else:
        consec = False
  consec = False
  for counter in values:
    for num in counter:
      if num == 8:
        if consec:
          shiplist[-1].append(num)
        else:
          shiplist.append([num])
        consec = True
      else:
        consec = False
  consec = False
  for counter in range(9):
    for num in values:
      if num[counter] == 8:
        if consec:
          shiplist[-1].append(num[counter])
        else:
          shiplist.append([num[counter]])
        consec = True
      else:
        consec = False

  remove = 0
  for counter in shiplist:
    if len(counter) == 1:
      remove += 1
      continue
    pure = []
    for iteration in counter:
        if iteration not in pure:
          pure.append(iteration)
    if len(counter) == 2:
      if counter[0] != 8:
        remove+=1
    if len(counter) == 3:
      if counter[0] != 2:
        remove += 1
    if len(counter) == 4:
      if counter[0] != 4:
        remove+=1
    if len(counter) == 5:
      if counter[0] != 6:
        remove+=1
        
    if len(counter) >= 5:
      if len(pure) == 2:
        shiplist.append([""])
      if len(pure) == 3:
        shiplist.append([""])
        shiplist.append([""])
      
  for counter in range(remove):
    shiplist.pop()

  shipcount = len(shiplist)
  return shipcount

def hitship(board,x):
  if board[x[0]][x[1]] == 3:
    board[x[0]][x[1]] = 2
  if board[x[0]][x[1]] == 5:
    board[x[0]][x[1]] = 4
  if board[x[0]][x[1]] == 7:
    board[x[0]][x[1]] = 6
  if board[x[0]][x[1]] == 9:
    board[x[0]][x[1]] = 8
  if board[x[0]][x[1]] == 0:
    board[x[0]][x[1]] = 1
    print()
    print("Miss!")
  else:
    print()
    print("Hit!")


winstate = 0
running = True
enemyinputlist = []
friendlysunken = 0
enemysunken = 0

#BOARD IDS:
#0 is empty
#1 is miss
#2 is hit3ship
#4 is hit4ship
#6 is hit5ship
#8 is hit2ship
#3 is 3ship
#5 is 4ship
#7 is 5ship
#9 is 2ship

#generates ships in both boards using generate function
boards = generate(boards, 3, 2, 3)
boards = generate(boards, 4, 1, 5)
boards = generate(boards, 5, 1, 7)
boards = generate(boards, 2, 1, 9)

#game loop
while running: 
  if winstate == 1:
    running = False

  drawboards(abclist,positions1,positions2)

  x = tuple_convert(input("Your input: "))
  print()
  print("Computing...")
  hitship(board2,x)

  time.sleep(1)
  savedenemysunken = enemysunken
  enemysunken = checkships(board2,enemysunken)
  if enemysunken > savedenemysunken:
    print()
    print("Ship down!")
  time.sleep(1)
  print()

  while True:
    z = abclist[random.randint(0,9)] + str(random.randint(0,9))
    if z not in enemyinputlist:
      enemyinputlist += z
      break

  print(f"Enemy input: {z}")
  time.sleep(1)
  z = tuple_convert(z)
  print()
  print("Computing...")

  time.sleep(1)
  hitship(board1,z)
  savedfriendlysunken = friendlysunken
  friendlysunken = checkships(board1,friendlysunken)
  if friendlysunken > savedfriendlysunken:
    print()
    print("Ship down!")
  time.sleep(1)
  print()
  print()
  print()
  if enemysunken == 5:
    whowon = 1
    running = False
  if friendlysunken == 5:
    whowon = 2
    running = False
if whowon == 1:
  print("GAME OVER")
  print()
  print("PLAYER WINS")
if whowon == 2:
  print("GAME OVER")
  print()
  print("COMPUTER WINS")