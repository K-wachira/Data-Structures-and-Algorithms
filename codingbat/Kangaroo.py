def kangaroo(x1, v1, x2, v2):
    yescount = 0
    nocount =0
    for i in range(0, 10000):
        x1 = x1 + v1
        x2 = x2 + v2


        if x1 == x2:
            yescount +=1
        else:
            nocount +=1


    if yescount >= 1:
        print("YES")
    else:
        print("NO")

x1= 0
v1= 3
x2 =4
v2 =2
kangaroo(x1, v1, x2, v2)