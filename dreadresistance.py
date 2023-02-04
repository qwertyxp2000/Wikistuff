import math

def stuff(d):
    print(d -1 - math.floor(0.1*d))
    print(d -2 - math.floor(0.15*d))
    print(d -3 - math.floor(0.2*d))
    print(d -4 - math.floor(0.25*d))
    print(d -5 - math.floor(0.3*d))
    
stuff(500)
stuff(2)
stuff(16)
stuff(34)

def stuff2(d):
    print(d -1 - math.ceil(0.1*d))
    print(d -2 - math.ceil(0.15*d))
    print(d -3 - math.ceil(0.2*d))
    print(d -4 - math.ceil(0.25*d))
    print(d -5 - math.ceil(0.3*d))
    
stuff2(500)
stuff2(2)
stuff2(16)
stuff2(34)
