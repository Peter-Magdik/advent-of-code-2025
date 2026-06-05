def invalid_ids_in_range(first: str, last: str) -> set[int]:
    result = set()

    max_digits = len(last)
    first, last = int(first), int(last)
    
    for unit_len in range(1, max_digits // 2 + 1):
        start_unit = 10 ** (unit_len - 1)
        end_unit = 10 ** unit_len

        for unit in range(start_unit, end_unit):
            s = str(unit)
            candidate_str = s + s
            while True:
                candidate = int(candidate_str)
                if candidate > last:
                    break
                if candidate >= first:
                    result.add(candidate)
                candidate_str += s

    return result

with open("day_02/input.txt", "r") as f:
    id_ranges = [id_range.split("-") for id_range in f.readline().strip().split(",") if id_range]

total = 0
for first, last in id_ranges:
    total += sum(invalid_ids_in_range(first, last))

print(total)