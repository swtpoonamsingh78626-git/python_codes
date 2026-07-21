no = 1
while no <= 100:
    print(no)
    no += 1
    

no = 100
while no >= 1:
    print(no)
    no -= 1
    

no = 5
while no <= 50:
    print(no)
    no += 5

no = [1, 4, 9, 16, 25, 36, 49, 64 ,81, 100]
i = 0
while i < len(no):
    print(no[i])
    i += 1

no = (1, 4, 9, 16, 25, 36, 49, 64 ,81, 100)   
n = 36
h = 0
while h < len(no):
    if(no[h] == n):
        print("found on index", h)
    else:
        print("finding...")
    h += 1
