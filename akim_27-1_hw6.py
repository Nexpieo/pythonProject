def proizvedenie(*args):
    answer = 1
    for i in args:
        answer *= i
    return answer
print(proizvedenie(2, 3, 4, 5))


def palindrome(word = "hello"):
    if word == word[::-1]:
        check = True
    else:
        check = False
    return check
# def palindrome(word = 'hello'):
#     return word == word[::-1]  #упрощенный и правильный вариант
print(palindrome())


def calculator(n1, operator, n2):
    if operator == '+':
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        return n1 / n2
    elif operator == "**":
        return n1 ** n2
    elif operator == "//":
        return n1 // n2
    elif operator == "%":
        return n1 % n2
print(calculator(2, "**", 3))