def knapsack(weights, values, capacity):
    n = len(weights)
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    print("DP Table:")
    for row in dp:
        print(row)

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    print("\nMax value:", dp[n][capacity])
    print("Selected item indices (0-based):", list(reversed(selected_items)))


weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5

knapsack(weights, values, capacity)
