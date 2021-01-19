# Find PI to the nth digit
# Calculating pi using Gregory-Leibniz Series and Nilakantha
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11...
from decimal import *
from typing import Union


def find_pi_gls(decimal_precision) -> tuple[str, Union[Decimal, str]]:  # GREGORY-LEIBNIZ SERIES
    pi = Decimal(4)
    x = Decimal(3)

    getcontext().prec = decimal_precision + 1

    for i in range(10 ** 3):
        if i % 2 == 0:  # for each even i
            pi -= 4 / x
        else:
            pi += 4 / x  # for each odd i
        x += 2
    return "Gregory-Leibniz Series: ", pi


def find_pi_nilakantha(decimal_precision) -> tuple[str, Union[Decimal, str]]:  # Nilakantha Series
    def seq(x) -> Decimal:
        return Decimal(x * (x + 1) * (x + 2))

    pi = Decimal(3)
    inc = Decimal(2)

    getcontext().prec = decimal_precision + 1
    for i in range(10 ** 3):
        if i % 2 == 0:
            pi += 4 / seq(inc)
        else:
            pi -= 4 / seq(inc)
        inc += 2
    return "Nilakantha Series:", pi


if "__main__" == __name__:
    precision = int(input("Number of digits: "))
    print(*find_pi_nilakantha(precision))
    print(*find_pi_gls(precision))
