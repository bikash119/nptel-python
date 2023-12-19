def selectionsort(list):
    # Start from the beginning of the list # loop1
    for start in range(len(list)):
        # assume that first element is the smallest
        minpos = start
        # loop from ith position to the last of the list
        # for each iteration of loop 1, the start will point to i
        for i in range(start,len(list)):
            # check if assumption of first element is the smallest holds good. If not keep a note of the position
            if list[minpos] > list[i]:
                minpos = i
        # swap the element at minpos with the element at start of the second loop.
        (list[minpos],list[start])=(list[start],list[minpos])