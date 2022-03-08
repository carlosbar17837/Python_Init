usdollaramt = input ("How many US Dollars do you have?")
usdollaramt = float(usdollaramt)
usdtolempiras = 24.58
conversion = usdollaramt * usdtolempiras
conversion = round(conversion,2)
conversion = str(conversion)
print ("You have L." + conversion + " Lempiras")