import random as r


def play_a():
    draw = 0
    uw = 0
    pcw = 0
    pcLives = 3
    uLives = 3
    choiceList = ['石头', '剪刀', '布']
    while pcLives > 0 and uLives > 0:
        print("1. 石头")
        print("2. 剪刀")
        print("3. 布")
        userChoice = (int(input("选择'石头','剪刀'或'布'（输入数字） ")))
        
        if userChoice != 1 and userChoice != 2 and userChoice != 3:
            print("Has to be 1,2 or 3")
        else:
            pcChoice = r.randint(1, 3)
            # Draw condition
            if userChoice == pcChoice:
                print("平局!!!")
                draw = draw + 1
                pass
            # When you lose
            elif userChoice == 1 and pcChoice == 2:
                print("你输了")
                print("计算机选了:", choiceList[pcChoice])
                pcw = pcw + 1
                uLives = uLives - 1
            elif userChoice == 2 and pcChoice == 3:
                print("你输了")
                print("计算机选了:", choiceList[pcChoice])
                pcw = pcw + 1
                uLives = uLives - 1
            elif userChoice == 3 and pcChoice == 1:
                print("你输了")
                print("计算机选了:", choiceList[pcChoice])
                pcw = pcw + 1
                uLives = uLives - 1
            # When you win
            elif userChoice == 1 and pcChoice == 3:
                print("你赢了!!!")
                print("计算机选了： ", choiceList[pcChoice])
                uw = uw + 1
                pcLives = pcLives - 1
            elif userChoice == 2 and pcChoice == 1:
                print("你赢了!!!")
                print("计算机选了： ", choiceList[pcChoice])
                uw = uw + 1
                pcLives = pcLives - 1
            elif userChoice == 3 and pcChoice == 2:
                print("你赢了!!!")
                print("计算机选了： ", choiceList[pcChoice])
                uw = uw + 1
                pcLives = pcLives - 1
            # The final output
            if uLives == 0:
                print("你真的输了")
                print("你赢了 ", str(uw), " 次")
                print("计算机赢了 ", str(pcw), " 次")
                print("有 ", str(draw), " 次平局")
            if pcLives == 0:
                print("你真的赢了")
                print("你赢了 ", str(uw), " 次")
                print("计算机赢了 ", str(pcw), " 次")
                print("有 ", str(draw), " 次平局")


def play_b():
    draw = 0
    uw = 0
    pcw = 0
    pcLives = 3
    uLives = 3
    choiceList = ['Rock', 'Paper', 'Scissors']
    while pcLives > 0 and uLives > 0:
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        userChoice = (int(input("Choose 'Rock','Paper' or ' Scissors' type the number you want: ")))
        
        if userChoice != 1 and userChoice != 2 and userChoice != 3:
            print("Has to be 0,1, or 2")
        else:
            pcChoice = r.randint(1, 3)
            # Draw condition
            if userChoice == pcChoice:
                print("Draw!!!")
                draw = draw + 1
                pass
            # When you lose
            elif userChoice == 0 and pcChoice == 2:
                print("HAHA, YOU LOST TO A BOT")
                print("The Bot chose:", choiceList[pcChoice])
                pcw = pcw + 1
                uLives = uLives - 1
            elif userChoice == 2 and pcChoice == 3:
                print("HAHA, YOU LOST TO A BOT")
                print("The Bot chose:", choiceList[pcChoice])
                pcw = pcw + 1
                uLives = uLives - 1
            elif userChoice == 3 and pcChoice == 1:
                print("HAHA, YOU LOST TO A BOT")
                print("The Bot chose:", choiceList[pcChoice])
                pcw = pcw + 1
                uLives = uLives - 1
            # When you win
            elif userChoice == 1 and pcChoice == 3:
                print("WOW, YOU ACTUALLY WON!!!")
                print("The bot chose ", choiceList[pcChoice])
                uw = uw + 1
                pcLives = pcLives - 1
            elif userChoice == 1 and pcChoice == 0:
                print("HOW, YOU ACTUALLY WON!!!")
                print("The bot chose ", choiceList[pcChoice])
                uw = uw + 1
                pcLives = pcLives - 1
            elif userChoice == 3 and pcChoice == 2:
                print("HOW, YOU ACTUALLY WON!!!")
                print("The bot chose ", choiceList[pcChoice])
                uw = uw + 1
                pcLives = pcLives - 1
            # The final output
            if uLives == 0:
                print("You're bad kid, you literally lost to a bot")
                print("You won ", str(uw), " time(s)")
                print("And the bot won ", str(pcw), " time(s)")
                print("And there was ", str(draw), " draw(s)")
            if pcLives == 0:
                print("You won, How")
                print("You won ", str(uw), " time(s)")
                print("And the bot won ", str(pcw), " time(s)")
                print("And there was ", str(draw), " draw(s)")


while True:
    print("1. The Asian way")
    print("2. The NoOb WaY")
    ask = int(input("Which way do you want???（Choose the number in the front） "))
    if ask == 1:
        play_a()
    if ask == 2:
        play_b()
    else:
        break
