def bestPriceFinder(prices):
    priceCount = [0] * 5001
    for price in prices:
        priceCount[price] += 1

    totalCustomers = len(prices)
    maxRevenue = 0
    bestFoundPrice = 0

    for price in range(5001):
        if priceCount[price] > 0:
            revenue = price * totalCustomers
            if revenue > maxRevenue:
                maxRevenue = revenue
                bestFoundPrice = price
            totalCustomers -= priceCount[price]

    return bestFoundPrice

import sys
input_data = sys.stdin.read().strip()
prices = list(map(int, input_data.split()))

print(bestPriceFinder(prices))