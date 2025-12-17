class VulnerableContract:
    def __init__(self):
        self.balance = 100

    def withdraw(self, amount, attacker_callback=None):
        if amount <= self.balance:
            if attacker_callback:
                attacker_callback(amount, self)  # re-entrancy exploit
            self.balance -= amount
            return amount
        return 0

class PatchedContract:
    def __init__(self):
        self.balance = 100

    def withdraw(self, amount, attacker_callback=None):
        if amount <= self.balance:
            self.balance -= amount  # state updated first
            if attacker_callback:
                attacker_callback(amount, self)
            return amount
        return 0