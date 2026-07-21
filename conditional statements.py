age = 10

if(age == 10):
    print("age = 10")

if(age >= 67):
    print("age > 10")

if(age <= 67):
    print("age < 10")

# QUESTION

marks = 86

if(marks > 90):
    print("grade - A")

elif(marks < 90 and marks > 80):
    print("grade - B")

elif(marks < 80 and marks > 70):
    print("grade - C")

elif(marks < 70):
    print("grade - D")

else:
    print("grade - F")


# HOMEWORK->
no_1 = (int(input("value:"))) 
no_2 = (int(input("value:")))
no_3 = (int(input("value:")))
no_4 = (int(input("value:")))

if(no_1 >= no_2 and no_1 >= no_3 and no_1 >= no_4):
    print("greateast value - no_1")

elif(no_2 >= no_1 and no_2 >= no_3 and no_2 >= no_4):
    print("greateast value - no_2")

elif(no_3 >= no_2 and no_3 >= no_1 and no_3 >= no_4):
    print("greateast value - no_3")

elif(no_4 >= no_2 and no_4 >= no_3 and no_4 >= no_1):
    print("greateast value - no_4")
