inputs = []

while True:
    try:
        inputs.append(list(input()))
    except:
        break

dp = [[0 for _ in range(len(inputs[0]))] for _ in range(len(inputs))]

for i in range(len(inputs)):
    for j in range(len(inputs[0])):
        if inputs[i][j] == "S":
           dp[i][j] = 1
        elif inputs[i][j] == "^":
            dp[i][j] = 0 
            if j-1 >= 0:
                dp[i][j-1] += dp[i-1][j]
            if j + 1 < len(inputs[0]):
                dp[i][j+1] += dp[i-1][j]
        else:
            dp[i][j] += dp[i-1][j]
    print(dp[i])
print(sum(dp[-1]))
# print(dp)