number_of_tabs = int(input())
salary = int(input())
website = ''
penalty = 0
total = 0

if 500 <= salary <= 1500:

    if number_of_tabs <= 10:

        for i in range(number_of_tabs):
            website = str(input())

            if website == 'Facebook':
                penalty += 150
            elif website == 'Instagram':
                penalty += 100
            elif website == 'Reddit':
                penalty += 50

        total = salary - penalty

        if total <= 0:
            print('You have lost your salary.')
        else:
            print(total)
