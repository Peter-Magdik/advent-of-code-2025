with open("day_02/input.txt", "r") as f:
    id_ranges = [id_range.split("-") for id_range in f.readline().split(",")]

invalid_ids = list()

for first, last in id_ranges:
    range_invalid_ids = set()
    last_len = len(last)
    for chunk_size in range(last_len // 2):
        chunk = "1" + "0" * chunk_size

        for multiplier in range(len(first) // len(chunk), len(last) // len(chunk) + 1):
            while (temp:=int(chunk * multiplier)) <= int(last):
                if temp >= int(first):
                    range_invalid_ids.add(temp)
                elif int(first) <= int(str(temp) + chunk) <= int(last):
                    range_invalid_ids.add(int(str(temp) + chunk))
                if len(chunk) < len(str(int(chunk) + 1)):
                    break
                chunk = str(int(chunk) + 1)
    invalid_ids.extend(range_invalid_ids)

# too high: 41662374103

print(sum(invalid_ids))