##################################
#
# Given a strign s, find if the string occurs in text t
#
# example match("bat", "I’m batman") is True
# This is the same thing as "bat" in "I’m batman"
#
# running time:
##################################
def match(s, text):
    '''
    >>> match("bat", "I'm batman")
    True
    >>> match("bat","I'm Superman")
    False
    '''
    j = 0
    for i in text:
        if s[j] == i:
            if j == len(s)-1:
                return True
            j += 1
        else:
            j = 0
    return False
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
