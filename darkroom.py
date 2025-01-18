# text adventure playground
# mr harrison 2018

# improvements needed:
# more rooms
# better winBanner proc
# "backpack" and object usage
# tasks to achieve using objects
# interaction with autonomous persons

# initialise data structures and variables
global rooms,rmName,rmDesc,rmObjects,rmDests,compass,backpack
rmName=0
rmDesc=1
rmObjects=2
rmDests=3
compass="NSEWUD"
VALIDCMDS = ["get","drop"]
backpack=[]

global currentRoom,lives
currentRoom = 0
lives = 9
winningRoom = 6

# rooms list of lists
# rooms: [name,desc,[objects], [destinations]]
# objects is a free list
# destinations: [N,S,E,W,U,D]
rooms = [
         ["lobby","a hotel lobby",["chair","table","note"],[1,2,3,4,-1,-1]],
         ["stairwell","stairwell up and down",[],[-1,0,-1,-1,5,6]],
         ["dining room","a dining room",["fork","knife","apple"],[0,7,-1,-1,-1,-1]],
         ["bar","the hotel bar",["bartender","drunk","glass"],[-1,-1,-1,0,-1,-1]],
         ["street","street outside the hotel",["newspaper","dog"],[-1,-1,0,-1,-1,-1]],
         ["1st","1st floor lobby",["fire extinguisher","tray"],[-1,-1,-1,-1,-1,1]],
         ["basement","the basement",["sack","bricks","crate of beer"],[-1,-1,-1,-1,1,-1]],
         ["conservatory","a hot windowed room",["palm tree","spade"],[2,-1,-1,-1,-1,-1]],
          ]


def showRoom(roomNum):
  rmData = rooms[roomNum]
  print("You are in the",rmData[rmName],"which is",rmData[rmDesc])
  print("You can see:", rmData[rmObjects])
  print("You are carrying:",backpack)
  print("You can go in these directions:")
  validDests = ""
  for i in range(6):
    dest = rmData[rmDests][i]
    if dest != -1:
      validDests += compass[i] + " "
  print(validDests)

def getMove(roomNum):
  rmData = rooms[roomNum]
  badCommand = True
  while badCommand:
    command = input("What next?")
    if len(command) == 1:
      dirNum = compass.find(command.upper())
      newRoom = rmData[rmDests][dirNum]
      if newRoom == -1:
        print("You can't go that way!")
      else:
        badCommand = False        
    else:
      action = command.split(" ")[0]
      if action == "get":
        objectWanted = command.split(" ")[1]
        rmData = rooms[roomNum]
        if objectWanted in rmData[rmObjects]:
          backpack.append(objectWanted)
          rmData[rmObjects].remove(objectWanted)
          newRoom = currentRoom
          badCommand = False
        else:
          print("Sorry, that object is not here!")
      else: 
        command = input("I don't know that command yet, what next?")
  return newRoom

def winBanner():
  print("   o____")
  print("   |\\//|")
  print("   |//\\|")
  print("   |")
  print("   |")
  print("You found the darkroom")
  print("You win!")

#main program

print("Welcome to 'darkroom' - a text adventure")
print("Your mission is to find the 'darkroom'")
playing = True
while playing:
  showRoom(currentRoom)
  if currentRoom == winningRoom:
    winBanner()
    playing = False
  else:
    newRoom = getMove(currentRoom)
    currentRoom = newRoom


      


