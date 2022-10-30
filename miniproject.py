import random
print("Winning rules of game:\n"
      +"Rock vs Paper=Paper wins\n"
      +"Rock vs Scissor=Rock wins\n"
      +"Paper vs Scissor=Scissor wins")

while True:
    print("enter choice \n 1.Rock \n 2.Paper \n 3.Scissor")
    cho=int(input())
    
    if cho>3 or cho<1:
        print("enter valid input")
    if cho==1:
        ch="Rock"
    elif cho==2:
        ch="Paper"
    else:
        ch="Scissor"
        
    print("user choice=",ch)
    print("now computers turn")
    com=random.randint(1,3)
    
    if com==1:
        com_chs='Rock'
    elif com==2:
        com_chs='Paper'
    else:
        com_chs='Scissor'
    print("computers choice =",com_chs)
    print(ch+"VS"+com_chs)
    if ch==com_chs:
        print("draw")
        result="Draw"
    
    if ((cho==1 and com==2) or( cho==2 and com==1)):
        print("paper wins")
        result="Paper"
    elif ((cho==1 and com==3) or (cho==3 and com==1)):
        print("rock wins")
        result="Rock"
    else:
        print("Scissor wins")
        result="Scissor"
        
    if result=="Draw":
        print("its tie")
    if result==ch:
        print("user wins")
    else:
        print("computer wins")
        
        
    print("wanna play again(Y/N")
    choice=input()
    if choice.upper()=='N':
        break

