name = input("Your monster name? ")
monster = {"name" : name, "power" : 100}

def startGame():
    choice = input("choose!! \n1.Eat 2.Status 3.Exit? ")

    if choice == '1':
        goEat()
    elif choice == '2':
        goStats()
    else:
        goExit()

def goEat():
    print("Nyam...Nyam...")
    print("Power +100")
    monster["power"] += 100
    startGame()

def goStats():
    print("Status ")
    print("Name : " + monster['name'])
    print("Power : " + str(monster['power']))
    startGame()

def goExit():
    print("I wanna sleep bye....")

startGame()