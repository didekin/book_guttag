def make_change(coin_vals, change):
    """
    parameters:
    - coin_vals is a list of positive ints and coin_vals[0] =1
    - change is a positive int,
    return:
    - the minimum number of coins needed to have a set of coins the values of which sum to change.

    Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3.
    """
    # Initialize a dp array where dp[i] will store the minimum coins for amount i
    if change <= 0 or not change.is_integer():
        raise ValueError('Change should be a positive integer')

    # dp[i] represents the minimum number of coins needed to make change for the amount i.
    dp = [float('inf')] * (change + 1)
    dp[0] = 0  # Base case: 0 coins needed for 0 amount

    for amount in range(1, change + 1):
        print(f'amount_in = {amount}')
        for coin in coin_vals:
            print(f'coin: {coin}')
            print(f'dp_in = {dp}')
            if coin <= amount:
                print(f'amount - coin = {amount - coin}')
                print(f'dp[amount]= {dp[amount]}, dp[amount - coin] = {dp[amount - coin]}')
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            print(f'dp_out = {dp}')
    return dp[change]


make_change([1, 5, 8], 11)