number_of_groups = int(input())

musala_percentage = 0
monblan_percentage = 0
kilimandjaro_percentage = 0
ktwo_percentage = 0
everest_percentage = 0

total_number_of_people = 0

total_number_of_people_for_musala = 0
total_number_of_people_for_monblan = 0
total_number_of_people_for_kilimandjaro = 0
total_number_of_people_for_ktwo = 0
total_number_of_people_for_everest = 0

for i in range(number_of_groups):
    number_of_people = int(input())
    total_number_of_people += number_of_people

    if number_of_people <= 5:
        total_number_of_people_for_musala += number_of_people

    elif 6 <= number_of_people <= 12:
        total_number_of_people_for_monblan += number_of_people

    elif 13 <= number_of_people <= 25:
        total_number_of_people_for_kilimandjaro += number_of_people

    elif 26 <= number_of_people <= 40:
        total_number_of_people_for_ktwo += number_of_people

    elif number_of_people >= 41:
        total_number_of_people_for_everest += number_of_people

musala_percentage = total_number_of_people_for_musala / total_number_of_people * 100
monblan_percentage = total_number_of_people_for_monblan / total_number_of_people * 100
kilimandjaro_percentage = total_number_of_people_for_kilimandjaro / total_number_of_people * 100
ktwo_percentage = total_number_of_people_for_ktwo / total_number_of_people * 100
everest_percentage = total_number_of_people_for_everest / total_number_of_people * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimandjaro_percentage:.2f}%')
print(f'{ktwo_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')
