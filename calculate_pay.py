"""
Set E - Quiz 05
Group Quiz
"""


def calculate_pay(hours, wage):
    """
    Calculate an employee’s weekly pay.

    :param hours: the number of hours the employee has worked for the week in integer
    :param wage: the employee’s hourly wage in integer
    :precondition: hours and wage parameters must be integers or zero
    :postcondition: calculate employee's weekly pay correctly
    :return: an employee's weekly pay
    >>> calculate_pay(10, 10)
    100
    >>> calculate_pay(50,10)
    1000
    """
    if hours <= 0 or wage <= 0:
        result = 0
        return result
    if 0 < hours <= 40:
        result = hours * wage
        return result
    if hours > 40:
        result = hours * (2 * wage)
        return result


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
