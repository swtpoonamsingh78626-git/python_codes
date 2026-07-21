# QUESTION-1 ->

no = (int(input("value:")))

rem = no % 2

if(rem == 0):
    print("even")
else:
    print("odd")

# QUESTION - 2 ->

A = (int(input("value:")))
B = (int(input("value:")))
C = (int(input("value:")))

if(A >= B and A >= C):
    print("greatest value - A")
elif(B >= A and B >= C):
    print("greatest value - B")
else:
    print("greatest value - C")

# QUESTION - 3 ->

NO = (int(input("value:")))

MULTI = NO % 7

if(MULTI == 0):
    print("True")
else:
    print("False")
