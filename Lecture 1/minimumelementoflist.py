##################################
#
# Find the smallest element of a list
#
# running time: O(n)
##################################
def minElem(l):
    smallest = l[0]
    for i in range(len(1,l)):
        if l[i] < smallest:
            smallest = l[i]
    return smallest