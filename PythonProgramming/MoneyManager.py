DATA = [[],[],[],[],[],[],[],[],[],[],[],[]]


while True:
    print("********************************")
    print("1. Retrieve")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Update")
    print("5. Exit")
    print("********************************")
    menu = int(input(">"))
    if menu == 1:
        yDeposit = 0
        yWithdrawal = 0
        i = 0
        while i < len(DATA):
            mDeposit = 0
            mWithdrawal = 0
            j = 0
            while j < len(DATA[i]):
                #입금액 필드와 출금액 필드를 동시에 나열하여 줄을 맞춤
                if DATA[i][j][1] >= 0 :
                    print("Date:",i+1,'/',DATA[i][j][0],"Deposit:",DATA[i][j][1],"Withdrawal:\t\t","Usage:",DATA[i][j][2],sep='\t')
                    mDeposit += DATA[i][j][1]
                else :
                    print("Date:", i + 1, '/', DATA[i][j][0],"Deposit:\t\t","Withdrawal:", DATA[i][j][1], "Usage:", DATA[i][j][2],sep='\t')
                    mWithdrawal += DATA[i][j][1]
                j += 1
            # 달별 입금액과 출금액 그리고 총합 출력
            print("Month:",i+1,"\t\tDeposit:", mDeposit,"Withdrawal:",mWithdrawal,"Total:",mDeposit+mWithdrawal,sep='\t')
            yDeposit += mDeposit
            yWithdrawal += mWithdrawal
            i += 1
        # 연간 입금액과 출금액 그리고 총합 출력
        print("Year\t\t\t\tDeposit:", yDeposit,"Withdrawal:",yWithdrawal,"Total:",yDeposit+yWithdrawal,sep='\t')

    elif menu == 2:
        Month = int(input("Month? "))
        Day = int(input("Day? "))
        Money = 0
        while Money <= 0:
            Money = int(input("Deposit Money? "))
        Usage = input("Usage? ")
        DATA[Month - 1].append([Day,Money,Usage])
        # 입력 후 정렬
        # 정렬 기준은 한 달 내에서 날짜 작은 순, 같은 날짜 안에서는 입금액 작은 순, 입금액이 0일 때는 출금액 작은 순
        DATA[Month-1].sort()

    elif menu == 3:
        Month = int(input("Month? "))
        Day = int(input("Day? "))
        Money = 0
        while Money >= 0:
            Money = -int(input("Withdrawal Money? "))
        Usage = input("Usage? ")
        DATA[Month - 1].append([Day, Money, Usage])
        # 입력 후 정렬.
        # 정렬 기준은 한 달 내에서 날짜 작은 순, 같은 날짜 안에서는 입금액 작은 순, 입금액이 0일 때는 출금액 작은 순
        DATA[Month - 1].sort()

    elif menu == 4:
        Month = int(input("Update Month? "))
        Day = int(input("Update Day? "))
        i = 0
        #모든 달을 검색하는 것은 에러가 발생했음. 입력 받은 달만 검토해서 입력 받은 날짜가 있는지 검사함.
        #또한 업데이트 기능의 특성 상 같은 날짜의 데이터는 입력 받지 않는다고 가정함.
        while i < len(DATA[Month-1]):
            if DATA[Month-1][i][0] == Day :
                break
            i += 1

        if i == len(DATA[Month-1]):
            print("No Data!!!")
        else:
            DATA[Month - 1][i][1] = int(input("Money? "))
            DATA[Month - 1][i][2] = input("Usage? ")

    elif menu == 5:
        print("Bye!")
        break