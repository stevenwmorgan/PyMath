From numpy import random
def play_game(): #Play the game
  s,c = 0.0,0
  print("Your numbers are:")
  while s <= 1:
    x = random.uniform(0,1)
    s += x
    c += 1
  Print("Your game lasted " + str(c) + " rounds")
