# generate pairs, then work on it"
import bisect

inputs = input().split(",")
inputs_changed = []

for input in inputs:
    if len(input) == 0:
        continue
    lo, hi = input.split("-")
    inputs_changed.append((int(lo), int(hi)))

def generate_invalid(len_str):
    all_nums = set()
    curr_len = 1

    while curr_len <= len_str//2:
        for num in range(10**(curr_len-1), 10 ** (curr_len)):
            i = 2
            while curr_len * i <= len_str:
                all_nums.add(str(num) * i)
                i+=1
        curr_len += 1

    return all_nums

arr = generate_invalid(10)
arr = sorted(list(map(int, arr)))

running_sum = 0
# running_pairs = []
for input in inputs_changed:
    lo, hi = input
    index = bisect.bisect_left(arr, lo) 
    # print(arr[index])

    while arr[index] <= hi:
        # running_pairs.append(arr[index])
        running_sum += arr[index]
        index += 1
# print(arr[:100])        
# print(running_pairs)
print(running_sum)