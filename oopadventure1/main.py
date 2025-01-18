from room import Room
from character import Enemy, Friend
from item import Item

cheese = Item("cheese")
cheese.set_description("A mouldy piece of cheese")
hammer = Item("hammer")
hammer.set_description("A claw hammer")

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.item = hammer
# kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a long oak table.")
dining_hall.item = cheese
# dining_hall.describe()

ballroom = Room("Ballroom")
ballroom.set_description("A fabulous ballroom with marble floor.")
# ballroom.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
current_room = dining_hall

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("You look tasty!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

jeff = Enemy("Jeff", "A dull teacher")
jeff.set_conversation("Anyone? Anyone? Bueller?")
jeff.set_weakness("gin")
jeff.set_asset("cheese")
ballroom.set_character(jeff)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Hi, I've got no body to talk to")
catrina.set_feeling("lonely")
kitchen.set_character(catrina)

backpack = []

dead = False
while not dead:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
      inhabitant.describe()
    command = input("what now?] ")
    print("--------")
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
      if inhabitant is None:
        print("Nobody to talk to here!")
      else:
        inhabitant.talk()
    elif command == "hug":
      if isinstance(inhabitant,Enemy):
        print("you can't hug an enemy, dude")
      else:
        inhabitant.hug()
    elif command[:3] == "get"
      get_item = command[4:]
      if current_room.item == get_item:
        print("You pick up the",get_item)
        backpack.append(get_item)
        current_room.item = None
      else:
        print("That item is not here")
    elif command == "fight":
      if inhabitant is None:
        print("Nobody to fight here!")
      else:
        fight_with = input("What do you want to fight with?] ")
        if fight_with in backpack:
          won = inhabitant.fight(fight_with)
          if won:
            asset = inhabitant.get_asset()
            if asset is not None:
              print("You take the",asset)
              backpack.append(asset)
              print("You have",backpack)
        else:
          print("You don't have the",fight_with)
        else:
          dead = True
    

      
    

    



