n = int(input())

for i in range(1, 10):

    for q in range(1, 10):

        for w in range(1, 10):

            for e in range(1, 10):

                if n % i == 0 and n % q == 0 and n % w == 0 and n % e == 0:
                    print(f'{i}{q}{w}{e}', end=' ')
