import  random
list = ['rock', 'paper', 'scissor']
while True:
    ucount = 0
    ccount = 0
    uc = int(input('''
Game Start....
    1)Yes
    2)No|Exit
    '''))

    if uc == 1:
        for i in range(1,6):
            userInput = int(input('''
1)Rock
2)Paper
3)Scissor
            '''))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "paper"
            elif userInput ==3:
                uchoice = "scissor"
            Cchoice = random.choice(list)
            if Cchoice == uchoice:
                print("Computer Choice", Cchoice)
                print("User Choise", uchoice)
                print("Game Drow")
                # ucount = ucount+1   #draw game adding the score +1
                # ccount = ccount+1   #otherwise remove line
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice =="paper"):
                print("Computer Choice", Cchoice)
                print("User Choise", uchoice)
                print("You Win...")
                ucount = ucount + 1
            else:
                print("Computer Choice", Cchoice)
                print("User Choise", uchoice)
                print("Computer Win")
                ccount = ccount + 1

        if ucount==ccount:
            print("Final Game Draw.....")
            print("User Count",ucount)
            print("Computer Count", ucount)
        elif ucount>ccount:
            print("Final you win the Game.....")
            print("User Count", ucount)
            print("Computer Count", ccount)
        else:
            print("Final Computer win the Game .....")
            print("User Count", ucount)
            print("Computer Count", ccount)

    else:
        break


























# import random
# list = ["rock", "paper", "scissor"]
#
# while True:
#     ucount = 0
#     ccount = 0
#     uc = int(input('''
#     Game Start
#     1)Yes
#     2)Exit |No
#     '''))
#
#     if uc == 1:
#         for i in range (1,6):
#             userinput = int(input('''Enter the choices..
#             1)Rock
#             2)Paper
#             3)Scissor
#             '''))
#
#             if userinput == 1:
#                 uchoise = "rock"
#             elif userinput == 2:
#                 uchoise = "paper"
#             elif userinput == 3:
#                 uchoise= "scissor"
#             cchoice = random.choice(1)
#             if cchoice == uchoise:
#             print("computer value:-", cchoice)
#             print("user value:-",uchoise)
#             print("Game Drown")
#             ccount = ccount+1
#             ucount = ucount+1
#             elif(uchoise=="rock" and cchoice=="scissor" ) or (uchoise=="papers" and cchoice=="rock") or (uchoise=="scissor" and cchoice == "paper"):
#               print("yon Win")
#               ucount= ucount+1
#             else:
        #          print("computer value:-", cchoice)
        #          print("user value:-", uchoise)
        #          print("Computer Win")
        #          ucount = ucount + 1
#     else:
#         print("invalid choice" )