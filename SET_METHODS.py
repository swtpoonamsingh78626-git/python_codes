# SET METHODS
s = {"abc", 5, 4.5, 67, 57, True}
set2 = {"you are good", 34}
set3 = {67, 57,"I HATE THESE NUMBERS"}

s.add("meow")
print(s)

s.remove(True)
print(s)

print(s.union(set2))

print(s.intersection(set3))

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.clear()
print(s)