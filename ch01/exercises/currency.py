rate = float(input("What is the current exchange rate for Euros to Dollars? "))
amount = float(input("How much money do you want to exchange? "))

total = amount * rate

result = total - 3.00
printed__result = round(result, 2)
print(printed__result)