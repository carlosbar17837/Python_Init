honduraspesos = input("How many Lempiras do you have ?")
honduraspesos = float(honduraspesos)
usdollar_value = 24.75
dollars = honduraspesos/usdollar_value
dollars = round(dollars, 2)
dollars =str(dollars)
print("You have $" + dollars + "USD")

