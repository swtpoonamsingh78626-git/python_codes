vedu1 = int(input("value: "))
vedu2 = int(input("value: "))
vedu3 = int(input("value: "))
av = ((vedu1 + vedu2 + vedu3)/3)
print(av)
if(vedu1 < 35 or vedu2 < 35 or vedu3 < 35):
    print("Fail ❌ (one subject below 35)")

elif(av >= 90):
    print("A Grade ⭐")

elif(av >= 75):
    print("B Grade 👍")

elif(av >= 50):
    print("C Grade 🙂")

else:
    print("Fail ❌")

