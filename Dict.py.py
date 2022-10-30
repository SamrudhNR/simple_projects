place=dict()
while True:
    print("1.add places")
    print("2.list all")
    print("3.find on distance")
    print("4.find on cost")
    print("5.break")
    
    ch=int(input())
    if ch==1:
        print("enter place,dist,cost")
        pla=input()
        dist=input()
        cost=input()
        place[pla]=[dist,cost]
        
    if ch==2:
        for i in place.keys():
            print("{0},{1}".format(i,place[i]))
            
    if ch==3:
        print("enter the distance")
        dist=input()
        c=0
        A=list(place.values())
        for i in A:
            if dist<=i[0]:
                c+=1
        if c==0:
                print("nono")
        else:
                print("{0} is found".format(c))
            
    if ch==4:
        print("enter cost")
        cost=input()
        flag=0
        A=list(place.values())
        for i in A:
            if i[1]<=cost:
                flag+=1
                
        if flag==0:
            print("no place")
        else:
            print("{0} palce found".format(flag))
            
    if ch==5:
        break