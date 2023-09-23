class Player:
  def play(self): 
    print("The player is playing cricket.")
    
class Batsman (Player):
  def play(self):
    print("The batsman is batting.")

class Bowler (Player):
  def play(self):
    print("The bowler is bowling.")

# create object of batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the Play method for each objects
batsman.play()
bowler.play()

