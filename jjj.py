sum=0
while(sum<100):
    print("player1")
    player1=int(input("enter the number"))
    sum+=player1
    print(sum)
    if (sum==100):
        print("player2 loser")
        break
    player2=int(input("enter the number"))
    sum+=player2
    print(sum)
    if (sum==100):
        print("player1 loser")
        break
    if(sum>100):
        print("no one winner")
