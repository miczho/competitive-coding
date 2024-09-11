"""
Problem Statement:
You are given three lists representing the attributes of customers at a bank. Each customer is identified by an index in these lists, and each list contains the following information:

credit_score: A list where the i-th element represents the credit score of the i-th customer.
account_balance: A list where the i-th element represents the account balance of the i-th customer.
income: A list where the i-th element represents the income of the i-th customer.


The bank uses these attributes to determine the overall risk of issuing a loan to customers. The risk is determined by sorting the customers based on the following criteria:

Primary Sort: Sort customers by credit score in descending order (higher credit scores are less risky).
Secondary Sort: If two or more customers have the same credit score, sort them by account balance in descending order (higher account balances are less risky).
Tertiary Sort: If there is still a tie, sort the customers by income in descending order (higher incomes are less risky).


Your task is to implement a function that returns the indices of the customers sorted by risk according to the guidelines above.


Input:
credit_score: A list of characters where each element represents a customer's credit score.
account_balance: A list of integers where each element represents a customer's account balance.
income: A list of integers where each element represents a customer's income.

Output:
A list of integers representing the indices of the customers sorted by their risk level according to the given criteria.


Input Data:
credit_score = ['A', 'D', 'B', 'D', 'C', 'A', 'E']
account_balance = [10000, 2000, 5000, 3000, 4500, 8000, 2500]
income = [90000, 45000, 60000, 40000, 70000, 85000, 35000]

#2024 #interview
"""

def get_best_users(credit_score, account_balance, income):
    n = len(credit_score)
    users = []

    for i in range(n):
        users.append((credit_score[i], -account_balance[i], -income[i], i))

    users.sort()

    return [user[3] for user in users]


credit_score = ['A', 'D', 'B', 'D', 'C', 'A', 'E']
account_balance = [10000, 2000, 5000, 3000, 4500, 8000, 2500]
income = [90000, 45000, 60000, 40000, 70000, 85000, 35000]

print(get_best_users(credit_score, account_balance, income))  # [0, 5, 2, 4, 3, 1, 6]
