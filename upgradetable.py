import math

#Base cost of the tower
basetower = 200

#The table of prices of the upgrades of that tower
upgrade_table = [
  [140, 220, 300, 1800, 15000],
  [100, 190, 400, 7500, 45000],
  [90, 200, 625, 2000, 21500]
]

#The table of sellbacks of the tower (in case of stuff like Favored Trades or Banana Salvage)
sellback_table = [
  [0.7, 0.7, 0.7, 0.7, 0.7],
  [0.7, 0.7, 0.7, 0.7, 0.7],
  [0.7, 0.7, 0.7, 0.7, 0.7],
]

#Difficulty multiplier for Easy, Medium, Hard, and Impoppable
difficulty_multiplier = [0.85, 1, 1.08, 1.2]

#Algorithm for the weird rounding stuff
def RoundToFive(num): #the annoying BTD6 rounding stuff
    num = math.floor(num)
    num = (num + 2.5)
    rem = num % 10
    if rem > 5:
        rem = rem - 5
    return round(num-rem)

#Write down table roundings
