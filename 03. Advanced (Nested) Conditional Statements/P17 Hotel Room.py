month = str(input())
number_of_nights = int(input())

apartment = 0
studio = 0
studio_discount = 0
apartment_discount = 0

if month == 'May' or month == 'June' or \
        month == 'July' or \
        month == 'August' or \
        month == 'September' or \
        month == 'October':

    if month == 'May' or month == 'October':
        studio = 50
        apartment = 65

        if number_of_nights > 14:
            studio_discount = studio * 0.30

        elif number_of_nights > 7:
            studio_discount = studio * 0.05

    elif month == 'June' or month == 'September':
        studio = 75.20
        apartment = 68.70

        if number_of_nights > 14:
            studio_discount = studio * 0.20

    elif month == 'July' or month == 'August':
        studio = 76
        apartment = 77

    if number_of_nights > 14:
        apartment_discount = apartment * 0.10

    total_price_for_studio = (studio - studio_discount) * number_of_nights
    total_price_for_apartment = (apartment - apartment_discount) * number_of_nights

    print(f'Apartment: {total_price_for_apartment:.2f} lv.')
    print(f'Studio: {total_price_for_studio:.2f} lv.')
