change = float(input())

coins = 0

change = int(change * 100)
total = change

while total > 0:

    if total >= 200:
        total -= 200
        coins += 1

    elif total >= 100:
        total -= 100
        coins += 1

    elif total >= 50:
        total -= 50
        coins += 1

    elif total >= 20:
        total -= 20
        coins += 1

    elif total >= 10:
        total -= 10
        coins += 1

    elif total >= 5:
        total -= 5
        coins += 1

    elif total >= 2:
        total -= 2
        coins += 1

    elif total >= 1:
        total -= 1
        coins += 1

print(coins)
