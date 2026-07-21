m1 = int(input("Sub1: "))  
m2 = int(input("Sub2: "))
m3 = int(input("Sub3: "))
m4 = int(input("Sub4: "))
m5 = int(input("Sub5: "))
m6 = int(input("Sub6: "))


if( m1 > 60 or m2 > 60 or m3 > 60 or m4 > 60 or m5 > 60 or m6 > 30 ):
    print("Invalid marks entered ❌")

p1 = (m1 / 60) * 100 
p2 = (m2 / 60) * 100
p3 = (m3 / 60) * 100
p4 = (m4 / 60) * 100
p5 = (m5 / 60) * 100
p6 = (m6 / 30) * 100


percentage = (p1 + p2 + p3 + p4 + p5 + p6) / 6

print("Percentage:", percentage)
