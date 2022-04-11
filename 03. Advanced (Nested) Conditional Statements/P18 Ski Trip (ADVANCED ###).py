number_of_days = int(input())
type_of_room = str(input())
rating = str(input())

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00

apartment_discount = 0
president_apartment_discount = 0
total_price_for_a_room = 0
total_price_for_apartment = 0
total_price_for_presidential_apartment = 0
additional_discount = 0
additional_pay = 0
room_with_discounts = 0
apartment_with_discounts = 0
president_apartment_with_discounts = 0
apartment1 = 0
president_apartment1 = 0

if type_of_room == 'room for one person' or type_of_room == 'apartment' or \
                                            type_of_room == 'president apartment':
    nights = number_of_days - 1

    if type_of_room == 'room for one person':

        total_price_for_a_room = room_for_one_person * nights

        if rating == 'positive':
            additional_pay = total_price_for_a_room * 0.25
            room_with_discounts = total_price_for_a_room + additional_pay

        elif rating == 'negative':
            additional_discount = total_price_for_a_room * 0.10
            room_with_discounts = total_price_for_a_room - additional_discount

        print(f'{room_with_discounts:.2f}')

    elif type_of_room == 'apartment':

        total_price_for_apartment = apartment * nights

        if number_of_days < 10:
            apartment_discount = total_price_for_apartment * 0.30

        elif 10 <= number_of_days <= 15:
            apartment_discount = total_price_for_apartment * 0.35

        elif number_of_days > 15:
            apartment_discount = total_price_for_apartment * 0.50

        apartment1 = total_price_for_apartment - apartment_discount

        if rating == 'positive':
            additional_pay = apartment1 * 0.25
            apartment_with_discounts = apartment1 + additional_pay

        elif rating == 'negative':
            additional_discount = apartment1 * 0.10
            apartment_with_discounts = apartment1 - additional_discount

        print(f'{apartment_with_discounts:.2f}')

    elif type_of_room == 'president apartment':

        total_price_for_presidential_apartment = president_apartment * nights

        if number_of_days < 10:
            president_apartment_discount = total_price_for_presidential_apartment * 0.10

        elif 10 <= number_of_days <= 15:
            president_apartment_discount = total_price_for_presidential_apartment * 0.15

        elif number_of_days > 15:
            president_apartment_discount = total_price_for_presidential_apartment * 0.20

            president_apartment1 = total_price_for_presidential_apartment - president_apartment_discount

        if rating == 'positive':
            additional_pay = president_apartment1 * 0.25
            president_apartment_with_discounts = president_apartment1 + additional_pay

        elif rating == 'negative':
            additional_discount = president_apartment1 * 0.10
            president_apartment_with_discounts = president_apartment1 - additional_discount

        print(f'{president_apartment_with_discounts:.2f}')
