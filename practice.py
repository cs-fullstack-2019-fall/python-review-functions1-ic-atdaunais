def main():
    maximum(50, 20, 100)
    printing_num(fav_num())
    print(aboveOrBelow100(fav_num()))
    print(evenOrOdd())
    print(challenge_func1(challenge_func2()))


def maximum(num1, num2, num3):
    # if num1 > num2 and num1 > num3:
    #     print(num1)
    # elif num2 > num1 and num2 > num3:
    #     print(num2)
    # elif num3 > num2 and num3 > num1:
    #     print(num3)
    num_array = [num1, num2, num3]
    print(max(num_array))


def fav_num():
    return int(input("What's your favorite number? "))


def printing_num(favorite):
    print(f"Your favorite number is {favorite}!")


def aboveOrBelow100(fave):
    if fave > 100:
        return f"{fave} is greater than 100!"
    elif fave < 100:
        return f"{fave} is less than 100!"
    elif fave == 100:
        return f"{fave} is equal to 100!"


def evenOrOdd():
    userInput = int(input("Enter a number. I will say if it's even or odd: "))
    if (userInput % 2) == 0:
        return f"{userInput} is an even number!"
    elif (userInput % 2) == 1:
        return f"{userInput} is an odd number!"


def challenge_func1(input):
    return challenge_func3(input)


def challenge_func2():
    return input("Enter a greeting word: ")


def challenge_func3(howdy):
    return f"{howdy} World!"


main()
