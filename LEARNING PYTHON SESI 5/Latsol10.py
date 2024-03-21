for i in range (5):
    for j in range (5,i,-1):
        if 1 % 2 == 0:
            if j % 2 ==0:
                print(2, end=" ")
            else :
                print(3, end=" ")
        else :
                if j % 2 == 1:
                    print(2, end=" ")
                else :
                    print(3, end=" ")
    print()
