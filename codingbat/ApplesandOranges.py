

def countApplesAndOranges(s, t, a, b, apples, oranges):
     #start

    # s--t is what i am looking for
    # a b= location of the trees apples and oranges respecitvely
    # add a to the list of apples
    # add b to the list of oranges
    #  check if there is any int in apples and oranges in s,t

     totalappledistance = []
     totalorangesdistance = []
     housedistance = []
     oran = 0
     apple = 0

     for i in apples:
         totalappledistance.append(i + a)
     for i in oranges:
         totalorangesdistance.append(i + b)

     for i in range(s, t + 1):
         housedistance.append(i)

     for i in totalappledistance:
         if i >= s and i <= t:
             apple += 1
     for i in totalorangesdistance:
         if i >= s and i <= t:
             oran += 1









s=7
t=10
a =4
b=12
apples = [2,3,-4]
oranges =[3,-2,-4]

countApplesAndOranges(s, t, a, b, apples, oranges)


