

import math
def numWaterBottles(numBottles, numExchange):

        totaldrunk = numBottles
        p = numBottles


        while p >= numExchange:
            totaldrunk += (p // numExchange)
            p = (p // numExchange )+ (p% numExchange)
        return totaldrunk




numBottles =10
numExchange =6
print(numWaterBottles(numBottles, numExchange))