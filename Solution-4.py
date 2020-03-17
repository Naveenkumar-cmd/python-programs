sales = int(input())

total_cost = 10*2000000+1000000

sales2 = sales*3000000

if sales2 > total_cost:
   print("Profit")
elif sales2 < total_cost:
   print("Loss")
else:
   print("Broke Even")
