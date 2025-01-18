class Character():
    # Create a character

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.asset = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weakness = None

  # Set and get the enemys weakness
  def set_weakness(self, weakness):
      self.weakness = weakness
  def get_weakness(self):
      return self.weakness

  # Set an asset that you can take if you kill this enemy
  def set_asset(self, asset):
      self.asset = asset
  def get_asset(self):
      return self.asset
  
  def fight(self, combat_item):
    if combat_item == self.weakness:
        print("You fend " + self.name + " off with the " + combat_item )
        fights_won += 1
        return True
    else:
        print(self.name + " crushes you, puny adventurer")
        return False

class Friend(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.feeling = None

  def set_feeling(self, feeling):
      self.feeling = feeling
  def get_feeling(self):
      return self.feeling

  def hug(self):
    print(self.name,"hugs you back!")