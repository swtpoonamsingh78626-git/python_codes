# QUESTION - 1 ->

M = []
M1 = (input("movie:"))
M2 = (input("movie:"))
M3 = (input("movie:"))
M.append(M1)
M.append(M2)
M.append(M3)
print(M)

# QUESTION - 2 ->

a = [1, 2, 3, 2, 1]
b = a.copy()
b.reverse()
if(a == b):
    print("true")
else:
    print("false")

c = [1, 2, 3, 4, 5]
d = a.copy()
d.reverse()
if(c == d):
    print("true")
else:
    print("false")

# QUESTION - 3 ->

marks = ("C", "D", "A", "A", "B", "B", "A")
print(marks.count("A"))

# QUESTION - 4 ->

marks = ["C", "D", "A", "A", "B", "B", "A"]
print(marks.sort())
print(marks)