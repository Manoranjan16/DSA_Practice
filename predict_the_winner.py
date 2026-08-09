def predict_winner(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Base case: only one number left, that player just takes it
    for i in range(n):
        dp[i][i] = nums[i]

    # Build up for increasing subarray lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Choose the option (take left or take right) that maximizes 
            # (my pick - opponent's best net score from what's left)
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
            
    return dp[0][n - 1] >= 0


print(predict_winner([1, 5, 2]))       # False (correct game-theory answer)
print(predict_winner([1, 5, 233, 7]))  # True
print(predict_winner([1, 2]))          # True ✅ this now gives what you expected