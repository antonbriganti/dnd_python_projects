import random

def roll():
    rolls = 0
    dm = 0
    player = -1
    total = 0
    i = 0

    for _ in range(100):
        while dm != player:
            dm = random.randint(1,100)
            player = random.randint(1,100)
            rolls += 1

        #print("It took", rolls, "rolls")
        total += rolls
        i += 1
        dm = 0
        player = -1
        rolls = 0

    print("average was", total//i, "rolls")
    return total/i

total_avg = 0
for _ in range(100):
    total_avg += roll()
print("total average was", total_avg//100, "rolls")
