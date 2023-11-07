def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def main():
    n = int(input("Enter the number of items: "))
    weights = list(map(int, input("Enter the weights of items: ").split()))
    values = list(map(int, input("Enter the values of items: ").split()))
    capacity = int(input("Enter the knapsack capacity: "))

    max_value = knapsack_01(weights, values, capacity)

    print("Maximum value that can be obtained:", max_value)

if __name__ == "__main__":
    main()
