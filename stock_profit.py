stocks=[6,13,2,10,3,5]
minimum=stocks[0]
profit=1
for i in range(len(stocks)):
    minimum=min(minimum,stocks[i])
    profit=max(profit,stocks[i]-minimum)

print(profit)
