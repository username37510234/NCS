def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money


balance = 0
balance = deposit(balance, 1000)


def withdraw(balance, money):
    if balance < money:
        print("{1}원 출금에 실패하였습니다. 잔액은 {0}원입니다.".format(balance,money))
        return balance
    else:
        print("{1}원 출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money,money))
        return balance-money


balance = withdraw(balance, 1500)
balance = withdraw(balance, 500)


def withdraw_night(balance, money):
    commission = 100
    withdraw(balance,money)
    return balance-commission

balance = withdraw_night(balance, 200)
