#Программа обменный пункт.
usd=330
eur=390
rub=6

money=int(input("Сколько тенге у тебя сегодня с собой: "))
currency=int(input("На что меняешь ? Укажи код (баксики - 101, цеевропа - 102, деревянные - 103): "))

if currency ==101:
    cache = round(money/usd, 2)#Округление до двух знаков после запятой. D182
    print("Ах ты жадная гадюка, не патриёт! Хавай капусту.")
    print("К получению: ", cache, " $")
elif currency ==102:
    cache = round(money/eur, 2)
    print("Эх, и ты туда-же, держи свои бумажки.")
    print("К получению: ", cache, " Euro")
elif currency ==103:
    cache = round(money/rub, 2)#Интересно, можно сколько угодно elif конструкций к одному if ? D0BE
    print("Ай маладца, дай пацелую!")
    print("К получению: ", cache, " рублей")
else:
    cache = 0
    print("Чё, сильно вумный штоле?!")