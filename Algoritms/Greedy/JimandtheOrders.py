import operator
n = input(); orders = dict()
for i in range(n):
    orders[i+1] = sum(map(int,raw_input().split()))

sorted_orders = sorted(orders.items(), key=operator.itemgetter(1))
for i in sorted_orders: print i[0],
