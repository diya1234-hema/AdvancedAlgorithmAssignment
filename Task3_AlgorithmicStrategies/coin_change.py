def coin_change_limited(coins, counts, target):

    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(len(coins)):

        coin = coins[i]
        count = counts[i]

        new_dp = dp[:]

        for amount in range(target + 1):

            if dp[amount] != float('inf'):

                for k in range(1, count + 1):

                    new_amount = amount + coin * k

                    if new_amount <= target:

                        new_dp[new_amount] = min(
                            new_dp[new_amount],
                            dp[amount] + k
                        )

        dp = new_dp

    if dp[target] == float('inf'):
        return "Impossible"

    return dp[target]


# Test Code

coins = [1, 2, 5]
counts = [3, 2, 1]
target = 7

result = coin_change_limited(
    coins,
    counts,
    target
)

print("Minimum Coins Needed:")
print(result)