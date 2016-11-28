class Scope:
    def __init__(self, parent=None):
        self.obj = {}
        self.parent = parent

    def __getitem__(self, key):
        if key in self.obj:
            return self.obj[key]
        else:
            return self.parent[key]

    def __setitem__(self, key, item):
        self.obj[key] = item


class Number:
    def __init__(self, value):
        self.value = value

    def evaluate(self, scope):
        return self


class Function:
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        answ = None
        for expr in self.body:
            answ = expr.evaluate(scope)
        return answ


class FunctionDefinition:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def evaluate(self, scope):
        scope[self.name] = self.function
        return self.function


class Conditional:
    def __init__(self, condtion, if_true, if_false=None):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false

    def evaluate(self, scope):
        answ = None
        if self.condition == 0:
            for expr in self.if_false:
                answ = expr.evaluate(scope)
        else:
            for expr in self.if_true:
                answ = expr.evaluate(scope)
        return answ


class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        temp = self.expr.evaluate(scope)
        print(temp.value)
        print('\n')
        return temp


class Read:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        temp = int(input())
        x = Number(temp)
        scope[self.name] = x
        return x


class FunctionCall:
    def __init__(self, fun_expr, args):
        self.fun_expr = fun_expr
        self.args = args

    def evaluate(self, scope):
        function = self.fun_expr.evaluate(scope)
        call_scope = Scope(scope)
        for expr, name in zip(self.args, function.args):
            call_scope[name] = expr.evaluate(scope)
        return function.evaluate(call_scope)


class Reference:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        return scope[self.name]


class BinaryOperation:
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def evaluate(self, scope):
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y,
               '%': lambda x, y: x % y,
               '==': lambda x, y: x == y,
               '!=': lambda x, y: x != y,
               '<': lambda x, y: x < y,
               '>': lambda x, y: x > y,
               '<=': lambda x, y: x <= y,
               '>=': lambda x, y: x >= y,
               '&&': lambda x, y: x and y,
               '||': lambda x, y: x or y}
        return Number(ops[self.op](self.lhs.evaluate(scope).value,
                                   self.rhs.evaluate(scope).value))


class UnaryOperation:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def evaluate(self, scope):
        num = self.expr.evaluate(scope).value
        if self.op == '-':
            return Number(-num)
        elif self.op == '!':
            return Number(not num)


if __name__ == '__main__':
    example()
    my_tests()
