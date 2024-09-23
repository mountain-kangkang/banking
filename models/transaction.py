class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
    
    def __str__(self) -> str:
        return f"{self.transaction_type} : {self.amount}\n잔고 :  {self.balance}"

    def to_tuple(self) -> tuple:
        return self.transaction_type, self.amount, self.balance


# test = Transaction("입금", 1000, 2000)
# print(test.__str__())
# print(test.to_tuple())