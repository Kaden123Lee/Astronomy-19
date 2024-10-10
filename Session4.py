class Favorite_Animal:
    def __init__(self, arm_leg, leg_leg, num_eyes, tail, fluffy):
        self.arm_length = arm_leg
        self.leg_length = leg_leg
        self.num_eyes = num_eyes
        self.tail = tail
        self.isfluffy = fluffy
fav1 = Favorite_Animal(arm_leg = 2.0, leg_leg = 4.0, num_eyes = 2, tail = False, fluffy = True)
print(f"Arm Length: {fav1.arm_length}")
print(f"Leg Length: {fav1.leg_length}")
print(f"Number of Eyes: {fav1.num_eyes}")
print(f"Has Tail?: {fav1.tail}")
print(f"Is Fluffy?: {fav1.isfluffy}")
