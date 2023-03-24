for row in range (7):
    for col in range (33):
        if ((col==1 or col==2 or col==3 or col==24) and row==0):
            print("*",end="")
        elif ((col==0 or col==4 or col==21 or col==23 or col==25)and row ==1):
            print("*",end="")
        elif((col==0 or col ==13 or col==23 or col==25)and row==2 ):
             print("*",end="")
        elif((col==0 or col==8 or col==9 or col==13 or col==14 or col==15 or col==17 or col==18  or col==23 or col==21 or col==25 or col==29 or col==30 ) and row==3):
             print("*",end="")
        elif((col==0  or col==3 or col==4 or col==5 or col==7 or col==10 or col==13 or col==16 or col==19 or col==21 or col==23 or col==25 or col==28 or col==31)and row==4):
           print("*",end="")
        elif((col==0 or col==4 or col==7 or col==10 or col==13 or col==16 or col==19 or col==21 or col==24 or col==28 or col==31)and row==5):
           print("*",end="")
        elif((col==1 or col==2 or col==3 or col==8 or col==9 or col==11 or col==13 or col==16 or col==19 or col==21 or col==24 or col==25 or col==26 or col==29 or col==30 or col==32)and row==6):
           print("*",end="")
        else:
            print(end=" ")
    print()

