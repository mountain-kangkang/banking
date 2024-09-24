from models.transaction import Transaction

class Account:
    def __init__(self) -> None:
        self.__balance = 10000
        self.transactions = []

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            self.transactions.append(Transaction("입금", amount, self.__balance))
        else:
            print("금액을 잘 못 입력하셨습니다.")

    def withdraw(self, amount: int) -> None:
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(Transaction("출금", amount, self.__balance))
        if amount <= 0:
            print("금액을 잘 못 입력하셨습니다.")
        if amount > self.__balance:
            print("계좌의 잔액이 부족합니다.")
# abc = Account()         # 인스턴스화(변수에 사용할 클래스 담기)