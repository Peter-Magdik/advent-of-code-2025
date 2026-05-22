with open("day_03/input.txt") as f:
    banks:list[list[int]] = []
    for bank in f.read().splitlines():
        banks.append(list(map(int, bank)))

"""
hladat maximu z pola ale vzdy 
len do indexu aby ostalo dostatocne vela cislic na dotvorenie cisla
"""

sum = 0
for bank in banks:
    digits_left = 12
    most_left_index = 0
    while digits_left > 0:
        max_digit = max(bank[most_left_index:len(bank) - (digits_left - 1)])
        sum += max_digit * (10 ** (digits_left - 1))
        digits_left -= 1
        most_left_index = bank.index(max_digit, most_left_index) + 1

print(sum)