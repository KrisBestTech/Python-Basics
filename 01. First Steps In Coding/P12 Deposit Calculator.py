deposited_sum = float(input())
months_to_deposit = int(input())
annual_rate = float(input()) / 100
sum = deposited_sum + months_to_deposit * ((deposited_sum * annual_rate)/ 12)
print(sum)