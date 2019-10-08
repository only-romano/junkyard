name = input("input your name: ")
print("Hello, " + name)

usd = 65
euro = 70
money = int(input("Input exchange sum: "))
currency = int(input("Input currency code ($ - 400; euro - 401): "))

if currency == 400:
    cash = round(money / usd, 2)
    print("Currency: US Dollars")
elif currency == 401:
    cash = round(money/euro, 2)
    print("Currency: euro")
else:
    cash = 0
    print("Currency: unknown")

print("Your exchanged cash:", cash)