import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll



while True:
    players = input("Enter a number of players(2-4):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter between 2-4")
    else:
        print("Invalid,please try again")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index +1,"Turn has started!")
        print("Your current score is ",player_score[player_index],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll(type y or n)")
            if should_roll.lower() == "y":
                value = roll()
                if value ==1:
                    print("You roll a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    print("You roll a :",value)
                    current_score += value
            else:
                break
            print("You current score is :", current_score)
        player_score[player_index] += current_score
        print("You total socre is :",player_score[player_index])

max_score = max(player_score)
winning_index = player_score.index(max_score)
print("Player number",winning_index +1,"is the winner with the score:",max_score)