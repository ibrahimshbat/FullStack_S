
def bigger(a,b):
    if a>b:
        return a
    else:
        return b

def biggest(a,b,c):
    max = bigger(a,b)
    if max>c:
        return max
    else:
        return c


print (biggest(5,4,9))
