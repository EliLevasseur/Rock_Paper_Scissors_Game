import random

player_pick = input("Please enter (rock/paper/scissors): ").lower()
bot_pick = random.randrange(1,3)

if bot_pick == 1:
    bot_pick = "rock"
elif bot_pick == 2:
    bot_pick = "paper"
else:
    bot_pick = "scissors"

print("Rock")
print("Paper")
print("scissors")

if bot_pick == "scissors" and player_pick == "paper" or bot_pick == "rock" and player_pick == "scissors" or bot_pick == "paper" and player_pick == "scissors":
    print("BOT HAS WON!")

else:
    print("USER HAS WON!")

print(bot_pick)




