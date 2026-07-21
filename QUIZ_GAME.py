print("lets get ready for the quiz! write your answers below.")
score = 0
print("first question - Riddle: What has keys but can't open locks?")
x = input("your answer is:").lower()
if(x == "keyboard"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is keyboard")

print("Riddle: The more you take, the more you leave behind. What am I?")
y = input("your answer is:").lower()
if(y == "footsteps" ):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is footsteps")

print("""Riddle: I speak without a mouth and hear without ears. I have no body,
 but I come alive with the wind. What am I?""")
z = input("your answer is:").lower()
if(z == "echo" ):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is echo")

print("Riddle: What has one eye but cannot see?")
a = input("your answer is:").lower()
if(a == "needle" ):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is needles")

print("Riddle: What gets wetter as it dries?")
b = input("your answer is:").lower()
if(b == "towel" ):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is towel")

print("Riddle: What can travel all around the world while staying in the same corner?")
c = input("your answer is:").lower()
if(c == "stamp"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is stamp")

print("Riddle: What comes once in a minute, twice in a moment, but never in a thousand years?")
d = input("your answer is:").lower()
if(d == "letter m"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is letter m")

print("Riddle: I have cities but no houses, forests but no trees, and rivers but no water. What am I")
e = input("your answer is:").lower()
if(e == "map" ):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is map")

print("Riddle: The person who makes it doesn't need it. The person who buys it doesn't use it. The person who uses it doesn't know they're using it. What is it?")
f = input("your answer is:").lower()
if(f == "coffin" ):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is coffin ")

print("Riddle: What is so fragile that saying its name breaks it?")
g = input("your answer is:").lower()
if(g == "silence"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is silence")

print("Riddle: I am always in front of you but can never be seen. What am I?")
h = input("your answer is:").lower()
if(h == "future"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is future")

print("Riddle: What has many teeth but cannot bite?")
i = input("your answer is:").lower()
if(i == "comb"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is comb")

print("Riddle: What has hands but cannot clap?")
j = input("your answer is:").lower()
if(j == "clock"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is clock")

print("Riddle: What goes up but never comes down?")
k = input("your answer is:").lower()
if(k == "age"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is age")

print("Riddle: A man looks at a painting and says,"
 "Brothers and sisters I have none, but that man's father is my father's son."
 " Who is in the painting?")
l = input("your answer is:").lower()
if(l == "his son"):
    print("correct answer")
    score += 1
else:
    print("wrong answer, the correct answer is his son")
print("your score is:",score,"/15")  
if score == 15:
    print("🏆 Perfect! You got all the answers correct!")
elif score >= 12:
    print("🌟 Excellent!")
elif score >= 9:
    print("👍 Good Job!")
elif score >= 6:
    print("😊 Nice Try!")
else:
    print("📚 Keep Practicing!")                                                                                                                                        