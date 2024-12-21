from webbrowser import Opera


systemProcess = True
expression = ""


class InvalidExpression(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


operators = ["+", "-"]


def eval(expression):
    for op in operators:
        expression = expression.replace(op, f"{op}")

    tokens = expression.split()

    if len(tokens) < 3 or len(tokens) % 2 == 0:
        raise InvalidExpression("Invalid expression")

    for i in range(len(tokens)):
        if i % 2 == 0:
            if not tokens[i].isdigit():
                raise InvalidExpression(f"Invalid number: {tokens[i]}")
        else:
            if tokens[i] not in operators:
                raise InvalidExpression(f"Invalid operator: {tokens[i]}")

    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i + 1])

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number

    return result


while systemProcess:
    expression = input("expr> ").strip()

    if expression.lower() == "exit":
        systemProcess = False
        break

    try:
        result = eval(expression)
        print(result)
    except InvalidExpression as e:
        print(e)
