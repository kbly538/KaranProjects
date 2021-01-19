# Problem statement:
# Start with a number n > 1.
# Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.

def calculate_steps(number):
    steps = 0
    number = number
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        steps += 1

    return steps


if "__main__" == __name__:
    user_input = int(input("Count down from: "))
    print(calculate_steps(user_input))
