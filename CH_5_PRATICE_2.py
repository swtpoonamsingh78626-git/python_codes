no = [1, 4, 9, 16, 25, 36, 49, 64 ,81, 100]
for y in no:
    print(y)

no = [1, 4, 9, 16, 25, 36, 49, 64 ,81, 100]
y = 81
k = 0
for g in no:
    if(g == y):
        print("found at index", k)
    else:
        print("finding...")
    k += 1