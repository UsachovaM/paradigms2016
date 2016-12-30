class Scope:
    def __init__(self, parent=None):
        self.var = {}
        self.parent = parent

    def __getitem__(self, key):
        if key in self.var:
            return self.var[key]
        else:
            return self.parent[key]

    def __setitem__(self, key, item):
        self.var[key] = item


class Number:
    def __init__(self, value):
        self.value = int(value)

    def evaluate(self, scope):
        return self

    def accept(self, visitor):
        return visitor.visit_number(self)


class Function:
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        answ = Number(0)
        if self.body is not None:
            for expr in self.body:
                answ = expr.evaluate(scope)
        return answ

    def accept(self, visitor):
        return visitor.visit_function(self)


class FunctionDefinition:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def evaluate(self, scope):
        scope[self.name] = self.function
        return self.function

    def accept(self, visitor):
        return visitor.visit_function_definition(self)


class Conditional:
    def __init__(self, condition, if_true, if_false=None):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false

    def evaluate(self, scope):
        answ = None
        if self.condition.evaluate(scope).value:
            if self.if_true is not None:
                for expr in self.if_true:
                    answ = expr.evaluate(scope)
        else:
            if self.if_false is not None:
                for expr in self.if_false:
                    answ = expr.evaluate(scope)
        return answ

    def accept(self, visitor):
        return visitor.visit_conditional(self)


class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        num = self.expr.evaluate(scope)
        print(num.value)
        return num

    def accept(self, visitor):
        return visitor.visit_print(self)


class Read:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        num = int(input())
        scope[self.name] = Number(num)
        return Number(num)

    def accept(self, visitor):
        return visitor.visit_read(self)


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

    def accept(self, visitor):
        return visitor.visit_function_call(self)


class Reference:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        return scope[self.name]

    def accept(self, visitor):
        return visitor.visit_reference(self)


class BinaryOperation:
    OPS = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x // y,
           '%': lambda x, y: x % y,
           '==': lambda x, y: x == y,
           '!=': lambda x, y: x != y,
           '<': lambda x, y: x < y,
           '>': lambda x, y: x > y,
           '<=': lambda x, y: x <= y,
           '>=': lambda x, y: x >= y,
           '&&': lambda x, y: x and y,
           '||': lambda x, y: x or y}

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def evaluate(self, scope):
        return Number(BinaryOperation.OPS[self.op](
                          self.lhs.evaluate(scope).value,
                          self.rhs.evaluate(scope).value))

    def accept(self, visitor):
        return visitor.visit_binary_operation(self)


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

    def accept(self, visitor):
        return visitor.visit_unary_operation(self)
