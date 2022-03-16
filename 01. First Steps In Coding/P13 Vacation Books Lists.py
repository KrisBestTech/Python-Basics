number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
time_per_book = number_of_pages // pages_per_hour
days = time_per_book / number_of_days
print(int(days))