import math

#Begin with the Beast Handler "base" costs of the base tower and its upgrades
beasthandler_cost = 250
beastupgrade_cost_medium = [
    [160, 810, 2010, 12500],
    [175, 830, 2065, 9500],
    [190, 860, 2120, 7800]
    ]
crosspath = [0, 0, 0]
beastpowermax = [1, 3, 8, 16]

#Difficulty multipliers
difficulty_multiplier = [0.85, 1, 1.08, 1.2]

def RoundToFive(num): #the annoying BTD6 rounding stuff
    num = math.floor(num)
    num = (num + 2.5)
    rem = num % 10
    if rem > 5:
        rem = rem - 5
    return round(num-rem)

def easyify(cost): #purpose is to make the Easy cost and do the annoying rounding junk afterwards
    cost = RoundToFive(cost * 0.85)
    return cost
def hardify(cost): #purpose is to make the Easy cost and do the annoying rounding junk afterwards
    cost = RoundToFive(cost * 1.08)
    return cost
def impoppableify(cost): #purpose is to make the Easy cost and do the annoying rounding junk afterwards
    cost = RoundToFive(cost * 1.2)
    return cost

#Whole Costs Table
beastupgrade_cost_table = []
for i in range(0, 4): #Easy, Medium, Hard, Impoppable
    beastupgrade_cost_table.append([ [], [], [] ]) #Start with appending an empty three-unit list, the three units for the Path 1-3 upgrades
    for j in range(0, len(beastupgrade_cost_medium)):
        for k in range(0, 4):
            beastupgrade_cost_table[i][j].append(RoundToFive(beastupgrade_cost_medium[j][k] * difficulty_multiplier[i]))
print(beastupgrade_cost_table)

#DEPRECATED
#-------------------------------------------------------------
#Easy Costs Table
beastupgrade_cost_easy = [ [], [], [] ]
for i in range(0, len(beastupgrade_cost_easy)):
    for j in range(0, 4):
               beastupgrade_cost_easy[i].append(easyify(beastupgrade_cost_medium[i][j]))
#Hard Costs Table (n.b. there's gotta be an easier way to write this junk)
beastupgrade_cost_hard = [ [], [], [] ]
for i in range(0, len(beastupgrade_cost_hard)):
    for j in range(0, 4):
               beastupgrade_cost_hard[i].append(hardify(beastupgrade_cost_medium[i][j]))
#Impoppable Costs Table (n.b. there's gotta be an easier way to write this junk)
beastupgrade_cost_impoppable = [ [], [], [] ]
for i in range(0, len(beastupgrade_cost_impoppable)):
    for j in range(0, 4):
               beastupgrade_cost_impoppable[i].append(impoppableify(beastupgrade_cost_medium[i][j]))
#-------------------------------------------------------------

##Testing that the tables are working as expected
#print(beastupgrade_cost_medium)
#print("-----------------------------------------------------------------")
#print(beastupgrade_cost_easy)
#print(beastupgrade_cost_medium)
#print(beastupgrade_cost_hard)
#print(beastupgrade_cost_impoppable)
#print("-----------------------------------------------------------------")

#Now to write the actual tables
print("|-")
for i in range(0, (len(beastupgrade_cost_medium))):
    for j in range(0, (len(beastupgrade_cost_medium[i]))):
        #these (i==0)*mathematics stuff are bool conditions, sorta like a compressed IF statement, also a non-newline ending with just a space
        print("|- %s-%s-%s" % ((i == 0) * (j + 1), (i == 1) * (j + 1), (i == 2) * (j + 1)), end = " ")
        #Hint: int() on a boolean results in 0 or 1 depending on false or true

        beast_summation = beasthandler_cost
        for k in range(0, j + 1):
            beast_summation += beastupgrade_cost_medium[i][k] 
        print("||", end = " ")
        print("$%s, %s power" % (beast_summation, beastpowermax[j]), end = " ")
        print("<br />", end = " ")
        print("$%s / %s power" % (round(beast_summation / beastpowermax[j], 4), beastpowermax[j]), end = " ")
        print("")
