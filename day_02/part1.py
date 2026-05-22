with open("day_02/input.txt", "r") as f:
    id_ranges = [id_range.split("-") for id_range in f.readline().split(",")]

invalid_ids = list()

for first, last in id_ranges:
    # auto skip
    if len(last) == len(first) and len(first) % 2 == 1:
        continue
    
    if len(first) == 1:
        potential_invalid_half = "1"
    else:
        potential_invalid_half = first[:len(first) // 2]
  
    while (temp:=int(potential_invalid_half + potential_invalid_half)) <= int(last):
        if temp >= int(first):
            invalid_ids.append(temp)
        potential_invalid_half = str(int(potential_invalid_half) + 1)

print(sum(invalid_ids))