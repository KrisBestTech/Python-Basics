name_of_city = str(input())
number_of_sales = float(input())

commission = 0

if name_of_city == 'Sofia' or \
        name_of_city == 'Varna' or \
        name_of_city == 'Plovdiv':

    if number_of_sales >= 0:

        if name_of_city == 'Sofia':
            if 0 <= number_of_sales <= 500:
                commission = number_of_sales * 0.05

            elif 500 <= number_of_sales <= 1000:
                commission = number_of_sales * 0.07

            elif 1000 <= number_of_sales <= 10000:
                commission = number_of_sales * 0.08

            elif number_of_sales > 10000:
                commission = number_of_sales * 0.12

        elif name_of_city == 'Varna':
            if 0 <= number_of_sales <= 500:
                commission = number_of_sales * 0.045

            elif 500 <= number_of_sales <= 1000:
                commission = number_of_sales * 0.075

            elif 1000 <= number_of_sales <= 10000:
                commission = number_of_sales * 0.10

            elif number_of_sales > 10000:
                commission = number_of_sales * 0.13

        elif name_of_city == 'Plovdiv':
            if 0 <= number_of_sales <= 500:
                commission = number_of_sales * 0.055

            elif 500 <= number_of_sales <= 1000:
                commission = number_of_sales * 0.08

            elif 1000 <= number_of_sales <= 10000:
                commission = number_of_sales * 0.12

            elif number_of_sales > 10000:
                commission = number_of_sales * 0.145

        print(f'{commission:.2f}')
    else:
        print('error')

else:
    print('error')
