import math

# GOLDEN EAGLE GRID
def grid_003(minimum, maximum):
    print("Golden Eagle...")
    print("")
    
    # Beast Power
    b_M = 24 # Max beast power
    b_m = 8 # Min beast power 
    b_c = b_m #Current beast power
    # Pierce
    p_M = 45 #Max pierce
    p_m = 15 #Min pierce
    p_c = p_m #Current pierce
    # Damage
    d_M = 6 #Max damage
    d_m = 2 #Min damage
    d_c = d_m #Current damage
    regrow_d_bonus = 1 #Regrow damage bonus

    #Pierce consumption and total "pierce" of heavier bloons: Ceramics, MOABs
    ceramic = 0 #Quantity of Ceramics picked up
    moab = 0 #Quantity of MOABs picked up

    # NOTE TO SELF: Perhaps it is better to not hardcode pierce consumptions into heavy bloon types; it should be a better idea to just make a ceramic_consumption etc. type variables and then softcode them from there...
    for i in range(minimum, maximum + 1):
        b_c = i #Increment the current beast power along the rows
        p_c = math.floor(p_m + (p_M - p_m)/(b_M - b_m) * (b_c - b_m)) # Calculate pierce
        d_c = math.floor(d_m + (d_M - d_m)/(b_M - b_m) * (b_c - b_m)) # Calculate damage
        ceramic = math.ceil(p_c/2) #calculate total max picks from pierce consumption of Ceramics
        moab = math.ceil(p_c/15) #calculate total max picks from pierce consumption of MOABs
        cooldown = round(0.6-(b_c-b_m)/(b_M-b_m) * 0.286796242, 4) # Rounds to 4dp
        
        print("|-")
        if (b_c == b_M):
            print("| %s || %s || %s (+%s Regrow) || %ss || Can pick up MOABs. Picks up to %s Ceramics, %s MOABs" % (i, p_c, d_c, regrow_d_bonus, cooldown, ceramic, moab))
        else:
            print("| %s || %s || %s (+%s Regrow) || %ss || Picks up to %s Ceramics" % (i, p_c, d_c, regrow_d_bonus, cooldown, ceramic))

    print("-------------------------------------------------")
    print("")

# GIANT CONDOR GRID
def grid_004(minimum, maximum):
    print("Giant Condor...")
    print("")
    
    # Beast Power
    b_M = 64 # Max beast power
    b_m = 16 # Min beast power 
    b_c = b_m #Current beast power
    # Pierce
    p_M = 90 #Max pierce
    p_m = 30 #Min pierce
    p_c = p_m #Current pierce
    # Damage
    d_M = 6 #Max damage
    d_m = 2 #Min damage
    d_c = d_m #Current damage
    moab_d_bonus = 11 #MOAB-class damage bonus
    regrow_d_bonus = 1 #Regrow damage bonus

    #Pierce consumption and total "pierce" of heavier bloons: Ceramics, MOABs, BFBs, targetable DDTs
    ceramic = 0 #Quantity of Ceramics picked up
    moab = 0 #Quantity of MOABs picked up
    bfb = 0 #Quantity of BFBs picked up
    ddt = 0 #Quantity of targetable DDTs picked up

    # NOTE TO SELF: Perhaps it is better to not hardcode pierce consumptions into heavy bloon types; it should be a better idea to just make a ceramic_consumption etc. type variables and then softcode them from there...
    for i in range(minimum, maximum + 1):
        b_c = i
        p_c = math.floor(p_m + (p_M - p_m)/(b_M - b_m) * (b_c - b_m))
        d_c = math.floor(d_m + (d_M - d_m)/(b_M - b_m) * (b_c - b_m))
        ceramic = math.ceil(p_c/2) #calculate total max picks from pierce consumption of Ceramics
        moab = math.ceil(p_c/15) #calculate total max picks from pierce consumption of MOABs
        bfb = math.ceil(p_c/45) #calculate total max picks from pierce consumption of BFBs
        ddt = math.ceil(p_c/50) #calculate total max picks from pierce consumption of targetable DDTs
        cooldown = round(0.6-(b_c-b_m)/(b_M-b_m) * 0.286796242, 4) # Rounds to 4dp
        
        print("|-")
        if (b_c == b_M): #the 64/64 case
            print("| %s || %s || %s (+%s MOAB-class, +%s Regrow) || %ss || Picks up to %s Ceramics, %s MOABs, %s BFBs, and %s (targetable) DDTs. Can target and damage any MOAB-class bloon." % (i, p_c, d_c, moab_d_bonus, regrow_d_bonus, cooldown, ceramic, moab, bfb, ddt))
        elif (ddt > 1): #the bigger DDT pickups case, which here is 33/64
            print("| %s || %s || %s (+%s MOAB-class, +%s Regrow) || %ss || Picks up to %s Ceramics, %s MOABs, %s BFBs, and %s (targetable) DDTs" % (i, p_c, d_c, moab_d_bonus, regrow_d_bonus, cooldown, ceramic, moab, bfb, ddt))
        else:
            print("| %s || %s || %s (+%s MOAB-class, +%s Regrow) || %ss || Picks up to %s Ceramics, %s MOABs, %s BFBs, and %s (targetable) DDT" % (i, p_c, d_c, moab_d_bonus, regrow_d_bonus, cooldown, ceramic, moab, bfb, ddt))
    print("-------------------------------------------------")
    print("")

# POUAKAI GRID
def grid_005(minimum, maximum):
    print("Pouakai...")
    print("")
    
    # Beast Power
    b_M = 132 # Max beast power
    b_m = 36 # Min beast power 
    b_c = b_m #Current beast power
    # Pierce
    p_M = 450 #Max pierce
    p_m = 150 #Min pierce
    p_c = p_m #Current pierce
    # Damage
    d_M = 90 #Max damage
    d_m = 10 #Min damage
    d_c = d_m #Current damage
    moab_d_bonus = 80 #MOAB-class damage bonus
    regrow_d_bonus = 1 #Regrow damage bonus

    #Pierce consumption and total "pierce" of heavier bloons: MOABs, BFBs, DDTs, ZOMGs
    moab = 0 #Quantity of MOABs picked up
    bfb = 0 #Quantity of BFBs picked up
    ddt = 0 #Quantity of DDTs picked up
    zomg = 0 #Quantity of ZOMGs picked up

    # NOTE TO SELF: Perhaps it is better to not hardcode pierce consumptions into heavy bloon types; it should be a better idea to just make a ceramic_consumption etc. type variables and then softcode them from there...
    for i in range(minimum, maximum + 1):
        b_c = i
        p_c = math.floor(p_m + (p_M - p_m)/(b_M - b_m) * (b_c - b_m))
        d_c = math.floor(d_m + (d_M - d_m)/(b_M - b_m) * (b_c - b_m))
        moab = math.ceil(p_c/10) #calculate total max picks from pierce consumption of MOABs
        bfb = math.ceil(p_c/30) #calculate total max picks from pierce consumption of BFBs
        ddt = math.ceil(p_c/30) #calculate total max picks from pierce consumption of DDTs
        zomg = math.ceil(p_c/50) #calculate total max picks from pierce consumption of ZOMGs
        cooldown = round(0.6-(b_c-b_m)/(b_M-b_m) * 0.286796242, 4) # Rounds to 4dp
        
        print("|-")
        print("| %s || %s || %s (+%s MOAB-class, +%s Regrow) || %ss || Picks up to %s MOABs, %s BFBs, %s ZOMGs, and %s DDTs" % (i, p_c, d_c, moab_d_bonus, regrow_d_bonus, cooldown, moab, bfb, zomg, ddt))
    print("-------------------------------------------------")
    print("")

# PRINTING GRIDS
grid_003(8, 24)
grid_004(16, 64)
grid_005(36, 132)
