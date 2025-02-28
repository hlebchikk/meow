#Магазин с булочками :)
Bun_price = 10
print("Hi! Buns cost 10 coins each. How many coins do you have?")
C = int(input("Coin:"))
print("How many buns do you want to buy?")
B = int(input("Buns:"))
BUNS = (C >= B * 10) * B
COIN = (C - (BUNS * 10))
print(f"Now you have {BUNS} buns and {COIN} coins in your backpack!")
