class Robot:
    maker = "Bright Bots"                    # (given) A: class variable, the same for every robot

    def __init__(self, name, model, battery):
        # TODO 1: store name, model and battery on self. A battery below 0
        #   becomes 0 and a battery above 100 becomes 100.
        self.name = name
        self.model = model
        self.battery = max(0, min(100, battery))

    def introduce(self):
        # TODO 2: return "Hi, I am <name>, a <model> robot made by <maker>.
        #   Battery: <battery>%" using self for every value.
        return f"Hi, I am {self.name}, a {self.model} robot made by {self.maker}. Battery: {self.battery}%"

    def charge(self, amount):
        # TODO 3: if amount is 0 or less, return "Charge amount must be
        #   positive." and change nothing. Otherwise add it to the battery, cap it at 100 and
        #   return "<name> charged to <battery>%".
        if amount <= 0:
            return "Charge amount must be positive."
        self.battery = min(100, self.battery + amount)
        return f"{self.name} charged to {self.battery}%"


# TODO 4: create tom (name "Tom", model "T-100", battery 40) and
#   jerry (name "Jerry", model "J-200", battery 120).
tom = Robot("Tom", "T-100", 40)
jerry = Robot("Jerry", "J-200", 120)

print(tom.introduce())                                         # (given) B
print(jerry.introduce())
print(tom.charge(50))                                          # (given) C: normal charge
print(tom.charge(30))                                          # (given)    edge: goes past 100
print(tom.charge(-5))                                          # (given)    edge: bad amount
