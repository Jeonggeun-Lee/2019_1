import random

num = random.randint(1,20)

i=1
while i<=5 :
    print(">",end="")
    ans = int(input())
    if ans == num :
        break
    elif ans > num :
        print("It is larger!")
    else :
        print("It is smaller!")
    i+=1

if i>5 :
    print("Game is over. The number is", num)
else :
    print("You win!")
