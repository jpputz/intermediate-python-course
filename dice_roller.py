import random

def main():
    dice_rolls = int(input("how many time you want to roll? "))
    dice_sum = 0
    for i in range(dice_rolls):
        roll = random.randint(1, 6)
        dice_sum = dice_sum + roll
        print(f"Your roll has been a {roll}")
    print(dice_sum)


if __name__== "__main__":
  main()