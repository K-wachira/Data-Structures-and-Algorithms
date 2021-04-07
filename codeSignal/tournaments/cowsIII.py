def cowsIll(cow, sickDay):
    total = 0
    totalsickDays =[]
    milklost = 0

    for _ in range(len(sickDay)-1):
        total +=sum(cow)

    print(total)

    for i in sickDay:
        for j in i:
            totalsickDays.append(j)


    for i in totalsickDays:
        milklost += cow[i]*3
    print(milklost)






cow = [2,3,1]
sickDay = [
 [],
 [0],
 [1, 2],
 [],
 []
]

print(cowsIll(cow, sickDay))