
import tableSelectScreen, Lir, indian
winLose = {
    1: False,
    2: False,
    3: False,
    4: False
}

def changeLevel(level):
    if (level is 1) and winLose[1] is False:
        print(1)
        win = Lir.GameLoop()
        if win is True:
            winLose[1] = True
        main()
    elif (level is 2) and winLose[2] is False:
        print(2)
        win = indian.gameLoop()
        if win is True:
            winLose[2] = True
        main()
    else:
        main()

def main():

    win = True
    for x in winLose.keys():
        if winLose[x] is False:
            win = False
    if win is True:
        print("Ooops")

    level = tableSelectScreen.gameLoop()
    print("Selam hacı naber.")

    changeLevel(level)

main()
