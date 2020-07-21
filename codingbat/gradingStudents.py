#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

grades =[70, 71 , 72, 73, 74, 75,76,77,78,79,80, 38, 33]
def gradingStudents(grades):
     for i in grades:
        det = 0
        lst = i%10
        if lst <= 5:
            det =5-lst
        elif lst > 5:
            det = lst- 5

        print(i)
        print("break")


        if i < 38:
            print(i)
        elif i >= 38:
            if lst > 5:
                if lst == 6:
                    print(i-1)
                elif lst == 7:
                    print(i-2)
                elif lst== 8:
                    print((i+2))
                elif lst == 9:
                    print(i+1)
                else:
                    print(i)
            else:
                if det ==1 :
                    print(i +1)
                elif det ==2 :
                    print(i+2)

                elif det ==4:
                    print(i-1)

                elif det == 3:
                    print(i-2)
                elif det == 0:
                    print(i)
                else:
                    print(i)
        print("done")

# 75
# 67
# 40
# 33
gradingStudents(grades)