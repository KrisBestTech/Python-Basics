product = str(input())

if product == 'apple' or product == 'cherry' or \
                         product == 'kiwi' or \
                         product == 'lemon' or \
                         product == 'grapes' or \
                         product == 'banana':
    print('fruit')
elif product == 'cucumber' or product == 'tomato' or \
                              product == 'pepper' or \
                              product == 'carrot':
    print('vegetable')

else:
    print('unknown')
