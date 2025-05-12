def find_min_distance(stalls,cows):
    stalls = sorted(stalls)
    max_distance = stalls[-1] - stalls[0]
    min_distance = 0
    for i in range(1,max_distance+1):
        if place(cows,i,stalls):
            min_distance = i
        else:
            break
    return min_distance

def place(cows,min_dist,stalls):
    last_placed = stalls[0]
    cows_placed = 1
    i = 1
    for i in range(1,len(stalls)):
        if stalls[i] - last_placed >= min_dist:
            cows_placed += 1
            last_placed = stalls[i]
    if cows_placed >= cows:
        return True 
    return False
    

stalls = [1,2,8,4,9]
cows = 3

print(find_min_distance(stalls,cows))