maxNum = 0 

inputs = []

def count_invalid(left, right, n):
    # count = 0 
    res = []
    
    if left[:n//2] == right[:n//2]:
        # print(left[:n//2], right[:n//2])
        # print(int(left[:n//2]))
        # print(int(left[n//2:]))
        if int(left[:n//2]) >= int(left[n//2:]):
            # print("YES")
            
            if int(right[:n//2]) <= int(right[n//2:]): 
                # print("NO")
                res.append(left[:n//2] * 2)
        return res

    if int(left[:n//2]) >= int(left[n//2:]):
        res.append(left[:n//2] * 2)

    curr = int(left[:n//2])
    right_max = int(right[:n//2])

    while curr < right_max-1:
        curr += 1
        res.append(str(curr) * 2)

    if int(right[:n//2]) <= int(right[n//2:]):
        res.append(right[:n//2] * 2)
    
    return res


    

inputs = input().split(",")
inputs_changed = []

for input in inputs:
    if len(input) == 0:
        continue
    lo, hi = input.split("-")
    inputs_changed.append((lo, hi))
 
print(inputs_changed)

tot_res = []
for input_range in inputs_changed:
    # print(input_range)
    left = input_range[0]
    right = input_range[1]
    while len(left) < len(right):
        if len(left) % 2 == 1:
            left = "1"+ "0" * len(left)
            continue
        
        curr_max = "9" * len(left)
        # print(curr_max, left)
        curr_extension = count_invalid(left, curr_max, len(left))
        # print(curr_extension)
        tot_res.extend(curr_extension)
        # print(tot_res)
        
        left = "1" + "0" * len(left)
        # print(curr_max)
    if len(left) % 2 == 0:
        curr_extension = count_invalid(left, right, len(left))
        tot_res.extend(curr_extension)
    # print(curr_extension)
    # print(tot_res)
print(tot_res)
tot_res = map(int, tot_res)
print(sum(tot_res))


# for changed in inputs_changed:

