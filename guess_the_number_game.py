
print("Welcome to guess the number game. Here you get 3 tries to guess the secret number. The secret number can be from 1-15. Enter the value at the option 'secret number', So good luck. This game is made by Yashvi Singh 6A, who is a python begginer.")

secret_number = 13
won = False  

for i in range(3): 
    player = int(input("secret number :")) 

    if player == secret_number: 
        print("🎉 You win! 100$ (fake 😄). The secret number was", secret_number ) 
        won = True
        break
    else: 
        print("You lose😢! better luck next time.")

if not won:
    print("😢 You lose! The secret number was", secret_number)

print("game over")