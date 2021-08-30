from numpy import result_type


def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
r1,r2=add_sub(5,9)  

print(r1,r2)