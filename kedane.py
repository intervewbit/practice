

def kedane(arr):
    max = 0
    max_ending_here = 0
    for a in arr:
        max_ending_here += a
        if(max_ending_here<=0):
            max_ending_here=0
        else:
            if(max_ending_here>max):
                max = max_ending_here
    
    print('Maximum is %d' % max)


arr = [8,-2,-4,9,-10,11]
kedane(arr)