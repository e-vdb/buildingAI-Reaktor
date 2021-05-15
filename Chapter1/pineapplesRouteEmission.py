portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# intermediate level exercice
def mainInt():
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    if set(route) == set(range(5)):
    
                        distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                        emissions = distance * co2
                        print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
mainInt()

# advance level exercice

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000

bestroute = [0,0, 0, 0, 0]

def emission(route):
    distance=0
    for i in range(len(route)-1):
        distance+=D[route[i]][route[i+1]]
    return distance*co2

def permutations(route, ports):
    global bestroute,smallest
    if len(ports)==0:
        if emission(route)<smallest:
            smallest=emission(route)
            bestroute=route
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]],ports[:i]+ports[i+1:])

def mainAdv():
    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))
    #print('{:.1f}'.format(distance(bestroute)*co2))
    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

mainAdv()
