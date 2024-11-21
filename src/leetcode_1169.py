"""
There should be an O(nlogn) solution to this at least, maybe even O(n)

https://leetcode.com/problems/invalid-transactions/

#2024 #revisit
"""

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """

        parsed_transactions = [
            {
                "name": t[0],
                "time": int(t[1]),
                "amount": int(t[2]),
                "location": t[3]
            }
            for transaction in transactions
            for t in [transaction.split(",")]
        ]
        result = []

        for i, t1 in enumerate(parsed_transactions):
            if t1["amount"] > 1000:
                result.append(transactions[i])
                continue

            for j, t2 in enumerate(parsed_transactions):
                if i == j:
                    continue
                elif (
                    t1["name"] == t2["name"]
                    and abs(t1["time"] - t2["time"]) <= 60
                    and t1["location"] != t2["location"]
                ):
                    result.append(transactions[i])
                    break

        return result
