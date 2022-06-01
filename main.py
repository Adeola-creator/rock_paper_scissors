import random
options= ["r", "p", "s"]
print("Where r is rock, p is paper and s is scissors")


while True:
    player_choice= input('Make a selection: ')
    comp_choice= random.choice(options)
    if player_choice in options:
        print("Player ({}): CPU ({})".format(player_choice,comp_choice))
        if player_choice == comp_choice:
            print("DRAW")
            continue
        elif player_choice =="r" and comp_choice == "s":
            print("Player wins!!!")
            break
        elif player_choice == "r" and comp_choice == "p":
            print("CPU wins!!!")
            break
        elif player_choice == "p" and comp_choice == "s":
            print("CPU wins!!!")
            break
        elif player_choice == "p" and comp_choice == "r":
            print("Player wins!!!")
            break
        elif player_choice == "s" and comp_choice == "r":
            print("CPU wins!!!")
            break
        elif player_choice == "s" and comp_choice == "p":
            print("Player wins!!!")
            break
    else:
        print("Error, {} is not an option".format(player_choice))                       

     