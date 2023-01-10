#practicing class in python 23/01/04
class Marine():
    # static
    total = 0
    def __init__(self, health, damage, attalkrange):
        self.health = health
        self.damage = damage
        self.attalkrange = attalkrange
        self.total += 1
    def getattalked(self, damage):
        self.health = self.health - damage

marine1 = Marine(60, 30, 2)
marine2 = Marine(100, 30, 2)
print(marine1.total)


marine1.getattalked(marine2.damage)

print(marine1.health)