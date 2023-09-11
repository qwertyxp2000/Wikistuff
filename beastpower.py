import math

# GIANT CONDOR GRID
def grid_004(minimum, maximum):
    # Beast Power
    b_M = 64
    b_m = 16
    b_c = b_m
    # Pierce
    p_M = 90
    p_m = 30
    p_c = p_m
    # Damage
    d_M = 6
    d_m = 2
    d_c = d_m
    moab_d_bonus = 11
    regrow_d_bonus = 1

    #Ceramics, MOABs, BFBs
    ceramic = 0
    moab = 0
    bfb = 0
    ddt = 0

    for i in range(minimum, maximum + 1):
        b_c = i
        p_c = math.floor(p_m + (p_M - p_m)/(b_M - b_m) * (b_c - b_m))
        d_c = math.floor(d_m + (d_M - d_m)/(b_M - b_m) * (b_c - b_m))
        ceramic = math.ceil(p_c/2)
        moab = math.ceil(p_c/10)
        bfb = math.ceil(p_c/30)
        ddt = math.ceil(p_c/50)
        cooldown = round(0.6-(p_c-p_m)/48*0.286796242, 4) # Rounds to 4dp
        
        print("|-")
        if (ddt > 1):
            print("| %s || %s || %s (+%s MOAB-class, +%s Regrow) || %ss || Picks up to %s Ceramics, %s MOABs, %s BFBs, and %s (targetable) DDTs" % (i, p_c, d_c, moab_d_bonus, regrow_d_bonus, cooldown, ceramic, moab, bfb, ddt))
        else:
            print("| %s || %s || %s (+%s MOAB-class, +%s Regrow) || %ss || Picks up to %s Ceramics, %s MOABs, %s BFBs, and %s (targetable) DDT" % (i, p_c, d_c, moab_d_bonus, regrow_d_bonus, cooldown, ceramic, moab, bfb, ddt))

grid_004(16, 64)
