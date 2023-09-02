class Player: 
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @staticmethod
    def deposit():
        while True: 
            amount = input("Enter amount to deposit: ")
            if amount.isdigit():
                amount = int(amount)
                if amount >= 10:
                    break
                else: 
                    print("Amount shouldn't be less than $10")
            else: 
                print("Invalid Entry")
        return amount

    def player_info(self):
        self.name = input("Enter name: ")
        self.balance = Player.deposit()

        return {self.name, self.balance}
