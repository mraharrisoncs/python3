class Room():

  def __init__(self,room_name):
    self.name = room_name   # passed as an argument on instantiation
    self.description = None # set with a setter method below
    self.linked_rooms = {}  # empty dictionary
    self.item = None
    self.character = None

  def set_name(self,room_name): # setter for room name (if needed)
    self.name = room_name

  def get_name(self): # getter for room name
    return self.name 

  def set_description(self,room_description): # setter for desc
    self.description = room_description

  def get_description(self): # getter for desc
    return self.description 

  def set_character(self,room_character): # setter for char
    self.character = room_character

  def get_character(self): # getter for char
    return self.character 

  def describe(self): # describing method
    print(self.description)

  def link_room(self, room_to_link, direction): # method to link rooms by updating
    self.linked_rooms[direction] = room_to_link # the linked_rooms dictionary
    # print(self.name + " linked rooms :" + repr(self.linked_rooms))

  def get_details(self):
    print(self.name)
    print(self.description)
    for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print( "The " + room.get_name() + " is " + direction)

  def move(self, direction):
    if direction in self.linked_rooms:
        return self.linked_rooms[direction]
    else:
        print("You can't go that way")
        return self

 

    
  


    