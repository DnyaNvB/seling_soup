from collections import defaultdict

def is_feasible(bills):
    cash_reserve = dict.fromkeys(bills)
    cash_reserve = defaultdict(int)

    for bill in bills:
        cash_reserve[bill] += 1
        change_needed = bill - 5

        while change_needed >= 20 and cash_reserve[20] > 0:
            cash_reserve[20] -= 1
            change_needed -= 20
        while change_needed >= 15 and cash_reserve[15] > 0:
            cash_reserve[15] -= 1
            change_needed -= 15   
        while change_needed >= 10 and cash_reserve[10] > 0:
            cash_reserve[10] -= 1
            change_needed -= 10
        while change_needed >= 5 and cash_reserve[5] > 0:
            cash_reserve[5] -= 1
            change_needed -= 5

        if change_needed > 0:
            print(f'cash_reserve: {cash_reserve}')
            return False

        print(f'bill: {bill}')
        print(f'change_needed: {change_needed}')
        print(f'cash_reserve: {cash_reserve}')
        print("---------------------------------------------------------------")

    return True

customer_money = list(map(int, input().split()))
print("---------------------------------------------------------------")
print(f'result: {"Yes" if is_feasible(customer_money) else "No"}')


# challenging test case:
# 5 5 5 10 15 10
# 5 5 10 5 15 10
# 5 10 15
# 5 5 5 10 25 5
# 5 5 5 10 25 15
# 5 10 5 5 5 10 10 15 5 5 15 20 15 10 10 10
