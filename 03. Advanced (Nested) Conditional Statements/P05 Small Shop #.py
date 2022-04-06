product = str(input())
city = str(input())
quantity = float(input())

if city == 'Sofia':
    if product == 'coffee':
        coffee = 0.50
        total_price = quantity * coffee
        print(total_price)

    elif product == 'water':
        water = 0.80
        total_price = quantity * water
        print(total_price)
    elif product == 'beer':
        beer = 1.20
        total_price = quantity * beer
        print(total_price)
    elif product == 'sweets':
        sweets = 1.45
        total_price = quantity * sweets
        print(total_price)
    elif product == 'peanuts':
        peanuts = 1.60
        total_price = quantity * peanuts
        print(total_price)
elif city == 'Plovdiv':
    if product == 'coffee':
        coffee = 0.40
        total_price = quantity * coffee
        print(total_price)
    elif product == 'water':
        water = 0.70
        total_price = quantity * water
        print(total_price)
    elif product == 'beer':
        beer = 1.15
        total_price = quantity * beer
        print(total_price)
    elif product == 'sweets':
        sweets = 1.30
        total_price = quantity * sweets
        print(total_price)
    elif product == 'peanuts':
        peanuts = 1.50
        total_price = quantity * peanuts
        print(total_price)
elif city == 'Varna':
    if product == 'coffee':
        coffee = 0.45
        total_price = quantity * coffee
        print(total_price)
    elif product == 'water':
        water = 0.70
        total_price = quantity * water
        print(total_price)
    elif product == 'beer':
        beer = 1.10
        total_price = quantity * beer
        print(total_price)
    elif product == 'sweets':
        sweets = 1.35
        total_price = quantity * sweets
        print(total_price)
    elif product == 'peanuts':
        peanuts = 1.55
        total_price = quantity * peanuts
        print(total_price)
