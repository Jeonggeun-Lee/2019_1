database = [[],[],[],[]]
while True :
    print('****************************************')
    print('1. Retrieve')
    print('2. Add')
    print('3. Delete')
    print('4. Update')
    print('5. Quit')
    print('****************************************')
    menu = int(input('>'))
    if menu == 2:
        database[0].append(input('Name?'))
        database[1].append(int(input('Korean Score?')))
        database[2].append(int(input('Math Score?')))
        database[3].append(int(input('English Score?')))
        print()
    elif menu == 1:
        if len(database[0])==0 :
            print("No Data!!\n")
        else :
            i=0
            while i<len(database[0]) :
                print(database[0][i], " Korean:", database[1][i], " points Math:", database[2][i], " points English:",database[3][i], " points" ,sep="")
                i+=1
            print()
    elif menu == 5:
        print('Bye!')
        break
    elif menu == 3:
        deleted_index = int(input('Delete No?'))-1
        if deleted_index < 0 or deleted_index >= len(database[0]) :
            print("번호가 범위를 벗어났습니다.")
        else:
            del database[0][deleted_index]
            del database[1][deleted_index]
            del database[2][deleted_index]
            del database[3][deleted_index]
            print("Deleted!\n")
    elif menu ==4:
        updated_index = int(input('Update No?'))-1
        if updated_index < 0 or updated_index >= len(database[0]) :
            print("번호가 범위를 벗어났습니다.")
        else :
            database[0][updated_index] = input('Name?')
            database[1][updated_index] = int(input('Korean score?'))
            database[2][updated_index] = int(input('Math score?'))
            database[3][updated_index] = int(input('English score?'))
            print("Update Name:",database[0][updated_index]," Korean:",database[1][updated_index]," points Math:",database[2][updated_index]," points English:",database[3][updated_index]," points",sep="")
            print()
