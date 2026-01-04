inputs = []
max_curr_len = 0 
while True:
    try:
        curr_input = input()
        max_curr_len = max(len(curr_input), max_curr_len)
        inputs.append(curr_input)
    except:
        break

# make ranges
last_input = inputs[-1]
ranges = []
l = 0 
for i in range(1, len(last_input)):
    if last_input[i] != " ":
        ranges.append((l, i-1))
        l = i
ranges.append((l, max_curr_len - 1))
operations = list(x for x in list(last_input.split(" ")) if x != "")

print(ranges)

tot = 0
for j, curr_range in enumerate(ranges):
    all_curr = []

    for i in range(curr_range[1], curr_range[0]-1, -1):
        curr = ""
        for row in range(len(inputs)-1):
            curr += inputs[row][i]
        curr = curr.strip()
        if len(curr) > 0: 
            all_curr.append(int(curr))
        print(curr)
    
    op = operations[j]
    running_sum = all_curr[0]
    if op == "*":
        for i in range(1, len(all_curr)):
            running_sum *= all_curr[i]

    else:
        for i in range(1, len(all_curr)):
            running_sum += all_curr[i]
    tot += running_sum
    print(j, curr_range, running_sum)
print(tot)
        
# for input in inputs:



# print(inputs)