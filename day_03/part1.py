with open("day_03/input.txt") as f:
    banks = []
    for bank in f.read().splitlines():
        banks.append(list(map(int, bank))) 

best_tens_banks = [max(bank[:-1]) for bank in banks]

sum = 0
for i in range(len(best_tens_banks)):
    sum += int(str(best_tens_banks[i]) + str(max(banks[i][banks[i].index(best_tens_banks[i]) + 1:])))

print(sum)