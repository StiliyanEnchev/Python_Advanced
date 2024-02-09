def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def power(num1, num2):
    return num1 ** num2

sign_mapper = {
    '+': add,
    '-': substract,
    '/': divide,
    '*': multiply,
    '^': power
}


def execute_expression(expression):
    num1_text, sign, num2_text = expression.split()
    num1 = float(num1_text)
    num2 = float(num2_text)

    return sign_mapper[sign](num1, num2)

