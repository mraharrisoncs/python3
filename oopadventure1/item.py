class Item():

  def __init__(self,item_name):
    self.name = item_name   # passed as an argument on instantiation
    self.description = None # set with a setter method below

  def set_name(self,item_name): # setter for room name (if needed)
    self.name = item_name

  def get_name(self): # getter for room name
    return self.name 

  def set_description(self,item_desc): # setter for desc
    self.description = item_desc

  def get_description(self): # getter for desc
    return self.description