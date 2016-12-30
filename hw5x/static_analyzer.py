from model import *


class PureCheckVisitor:
    def visit(self, tree):
        return tree.accept(self)

    def visit_number(self, tree):
        return True

    def visit_function(self, tree):
        if tree.body:
            return all([self.visit(x) for x in tree.body])
        else:
            return True

    def visit_function_definition(self, tree):
        return self.visit(tree.function)

    def visit_conditional(self, tree):
        if tree.if_true:
            list_true = all([self.visit(x) for x in tree.if_true])
        else:
            list_true = True
        if tree.if_false:
            list_false = all([self.visit(x) for x in tree.if_false])
        else:
            list_false = True
        return list_true and list_false and self.visit(tree.condition)

    def visit_print(self, tree):
        return False

    def visit_read(self, tree):
        return False

    def visit_function_call(self, tree):
        if tree.args:
            res = all([self.visit(x) for x in tree.args])
            return res and self.visit(tree.fun_expr)
        else:
            return self.visit(tree.fun_expr)

    def visit_reference(self, tree):
        return True

    def visit_binary_operation(self, tree):
        return self.visit(tree.lhs) and self.visit(tree.rhs)

    def visit_unary_operation(self, tree):
        return self.visit(tree.expr)


class NoReturnValueCheckVisitor:
    def visit(self, tree):
        return tree.accept(self)

    def visit_number(self, tree):
        return True

    def visit_function(self, tree):
        if not tree.body:
            return False
        else:
            return [self.visit(x) for x in tree.body][-1]

    def visit_function_definition(self, tree):
        if not self.visit(tree.function):
            print(tree.name)
        else:
            return True

    def visit_conditional(self, tree):
        if tree.if_true:
            list_true = [self.visit(x) for x in tree.if_true][-1]
        else:
            list_true = False
        if tree.if_false:
            list_false = [self.visit(x) for x in tree.if_false][-1]
        else:
            list_false = False
        return list_true and list_false and self.visit(tree.condition)

    def visit_print(self, tree):
        return self.visit(tree.expr)

    def visit_read(self, tree):
        return True

    def visit_function_call(self, tree):
        if tree.args:
            return all([self.visit(x) for x in tree.args])
        else:
            return True

    def visit_reference(self, tree):
        return True

    def visit_binary_operation(self, tree):
        return self.visit(tree.lhs) and self.visit(tree.rhs)

    def visit_unary_operation(self, tree):
        return self.visit(tree.expr)
