budget = float(input())
season = str(input())

place = str
hotel_or_camp = str
cost_of_the_vacation = 0

if season == 'summer' or season == 'winter':

    if budget <= 100:
        place = 'Bulgaria'

        if season == 'summer':
            cost_of_the_vacation = budget * 0.30
            hotel_or_camp = 'Camp'

        elif season == 'winter':
            cost_of_the_vacation = budget * 0.70
            hotel_or_camp = 'Hotel'

    elif budget <= 1000:
        place = 'Balkans'

        if season == 'summer':
            cost_of_the_vacation = budget * 0.40
            hotel_or_camp = 'Camp'

        elif season == 'winter':
            cost_of_the_vacation = budget * 0.80
            hotel_or_camp = 'Hotel'

    elif budget > 1000:
        place = 'Europe'
        cost_of_the_vacation = budget * 0.90
        hotel_or_camp = 'Hotel'

    print(f'Somewhere in {place}')
    print(f'{hotel_or_camp} - {cost_of_the_vacation:.2f}')
