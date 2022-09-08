import random

i = 1
print(i)
isPlayerTurn = True

while i<20 :
    if isPlayerTurn == True :
        while True :
            print(">",end="")
            s = input()
            listOfNums = s.split()

            if len(listOfNums) == 1 :
                if int(listOfNums[0]) == i+1 :
                    i += 1
                    break
            elif len(listOfNums) == 2 :
                if int(listOfNums[0]) == i+1 and int(listOfNums[1])==i+2 :
                    i += 2
                    break

    elif isPlayerTurn == False :

        num = random.randint(1,2)
        if i == 19 :
            num = 1

        if num == 1:
            i+=1
            print(i)

        elif num == 2:
            i += 1
            print(i,end=" ")
            i += 1
            print(i)
    isPlayerTurn = not isPlayerTurn

if isPlayerTurn == True :
    print("You win!")
else :
    print("Computer win!")