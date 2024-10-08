from lawnmower import lawnmower
from left_to_right import leftToRight

def main():
    print("Give me a number n that will determine how long the list is:\n")
    n = int(input())
    print("Which algorithm would you like to user? (leftToRight(1) or Lawnmower(0))\n")
    if (input() == "1"):
        result = leftToRight(n)
    else:
        result = lawnmower(n)

    print(result)

if __name__ == "__main__":
    main()