tri_list = [1, 1, 1]
num = 0

dp = [i for i in tri_list]

if num < 4 :
    print([dp[i] for i in range(num)])

else:
    for item in range(3, num):
        dp.append(dp[item-1] + dp[item-2] + dp[item-3])

    print(dp)


