'''class mango:
    def _int_(self):
        print("hello")
    def balaji(self):
        print("this is without para")
            
    def shetty(self,a,b):
        print(a+b,"this is with para")
    def magicalprime(self,a):
        print("check it magicl prime or not ")
    def neon(self,a):
        print("check neon or not")
        


man=mango()
man.balaji()
man.shetty(10,20.5)
man.magicalprime(101)
man.neon(7)'''

#bankingproject using class
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty):
        amount=int(input("enter amount to withdraw"))
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")
            file=open("text.txt","a")
            file.write(f"Withdrawal: ${amount}")
            file.close()

    def deposit(self):
̣      amount=int(input("enter the amount"))
         file=open("nandan.txt","a")
        file.write(f"Withdrawal: ${amount}")
        file.close()


    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

# Example usage:
account = BankAccount(1000)
print("Balance:", account.get_balance())
account.deposit()
account.withdraw()
account.withdraw()
print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())
                        
