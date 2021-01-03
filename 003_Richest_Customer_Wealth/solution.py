class Solution:
    # Iterate, sum each customer's accounts and update max_wealth 
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = 0
            for money in customer:
                wealth += money
            if max_wealth < wealth:
                max_wealth = wealth
        return max_wealth
