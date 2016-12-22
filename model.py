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
        self.value = int(value)

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
        if self.condition.evaluate(scope):
            for expr in self.if_true:
                answ = expr.evaluate(scope)
        else:
            for expr in self.if_false:
                answ = expr.evaluate(scope)
        return answ


class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        num = self.expr.evaluate(scope)
        print(num.value)
        return num


class Read:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        num = int(input())
        scope[self.name] = Number(num)
        return Number(num)


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
        self.OPS = {'+': lambda x, y: x + y,
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

    def evaluate(self, scope):
        return Number(self.OPS[self.op](self.lhs.evaluate(scope).value,
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


def example():
    parent = Scope()
    parent["foo"] = Function(('hello', 'world'),
                             [Print(BinaryOperation(Reference('hello'),
                                                    '+',
                                                    Reference('world')))])
    parent["bar"] = Number(10)
    scope = Scope(parent)
    assert 10 == scope["bar"].value
    scope["bar"] = Number(20)
    assert scope["bar"].value == 20
    print('It should print 2: ', end=' ')
    FunctionCall(FunctionDefinition('foo', parent['foo']),
                 [Number(5), UnaryOperation('-', Number(3))]).evaluate(scope)


def testBinOp():
    parent = Scope()
    x = Number(42)
    y = Number(-17)
    z = Number(3)
    p = Number(0)
    assert 25 == BinaryOperation(x, '+', y).evaluate(parent).value
    assert 59 == BinaryOperation(x, '-', y).evaluate(parent).value
    assert -51 == BinaryOperation(z, '*', y).evaluate(parent).value
    assert 14 == BinaryOperation(x, '/', z).evaluate(parent).value
    assert 2 == BinaryOperation(UnaryOperation('-', y), '%',
                                z).evaluate(parent).value
    assert 0 == BinaryOperation(x, '==', z).evaluate(parent).value
    assert 1 == BinaryOperation(x, '!=', z).evaluate(parent).value
    assert 0 == BinaryOperation(x, '<', z).evaluate(parent).value
    assert 0 == BinaryOperation(x, '<=', y).evaluate(parent).value
    assert 1 == BinaryOperation(x, '>=', z).evaluate(parent).value
    assert 1 == BinaryOperation(z, '>', y).evaluate(parent).value
    assert 0 == BinaryOperation(p, '&&', z).evaluate(parent).value
    assert 0 == BinaryOperation(p, '||',
                                UnaryOperation('!', x)).evaluate(parent).value


def my_tests():
    testBinOp()


if __name__ == '__main__':
    example()
    my_tests()
