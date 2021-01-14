# a traveler is at the start of the grid he need to move to the end of the grid
#  how many ways the are their from start to end if the traveler can move only right and down 


def gridTraveler(i, j, memo={}):
    if i == 0 or j == 0:
        memo.update({(i, j): 0})
        return 0

    elif i == 1 and j == 1:
        memo.update({(i, j): 1})
        return 1

    else:
        if (i, j) in memo.keys():
            return memo[(i, j)]
        elif (j, i) in memo.keys():
            return memo[(j, i)]
        else:
            memo.update({(i, j): gridTraveler(i - 1, j, memo) + gridTraveler(i, j - 1, memo)})
            return memo[(i, j)]


print(gridTraveler(550, 50))
