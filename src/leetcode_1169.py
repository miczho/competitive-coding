"""
https://leetcode.com/problems/invalid-transactions/

#2024
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


    def invalidTransactions2(self, transactions: list[str]) -> list[str]:
        """
        Chàtġpţ's proposed solution
        """

        parsed_transactions = [
            (
                t.split(",")[0],
                int(t.split(",")[1]),
                int(t.split(",")[2]),
                t.split(",")[3],
                i,
            )
            for i, t in enumerate(transactions)
        ]

        parsed_transactions.sort(key=lambda x: x[1])

        invalid_set = set()

        for i, (name, time, amount, location, idx) in enumerate(parsed_transactions):
            if amount > 1000:
                invalid_set.add(idx)

            for j in range(i + 1, len(parsed_transactions)):
                if parsed_transactions[j][1] - time > 60:
                    break

                if (
                    parsed_transactions[j][0] == name
                    and parsed_transactions[j][3] != location
                ):
                    invalid_set.add(idx)
                    invalid_set.add(parsed_transactions[j][4])

        return [transactions[i] for i in invalid_set]
