from model import *


class PureCheckVisitor:
    def visit(self, tree):
        return tree.accept(self)

    def visit_number(self, tree):
        return True

    def visit_function(self, tree):
        return all([self.visit(x) for x in tree.body])

    def visit_function_definition(self, tree):
        return self.visit(tree.function)

    def visit_conditional(self, tree):
        list_true = all([self.visit(x) for x in tree.if_true])
        list_false = all([self.visit(x) for x in tree.if_false])
        return list_true and list_false and self.visit(tree.condition)

    def visit_print(self, tree):
        return False

    def visit_read(self, tree):
        return False

    def visit_function_call(self, tree):
        res = all([self.visit(x) for x in tree.args])
        return res and self.visit(tree.fun_expr)

    def visit_reference(self, tree):
        return True

    def visit_binary_operation(self, tree):
        return self.visit(tree.lhs) and self.visit(tree.rhs)

    def visit_unary_operation(self, tree):
        return self.visit(tree.expr)


class NoReturnValueCheckVisitor:
    def visit_body(self, list_t):
        if list_t:
            res = [self.visit(x) for x in list_t][-1]
        else:
            res = False
        return res
    
    def visit(self, tree):
        return tree.accept(self)

    def visit_number(self, tree):
        return True

    def visit_function(self, tree):
        return self.visit_body(tree.body)

    def visit_function_definition(self, tree):
        if not self.visit(tree.function):
            print(tree.name)
        return True

    def visit_conditional(self, tree):
        res_t = self.visit_body(tree.if_true)
        res_f = self.visit_body(tree.if_false)
        return res_t & res_f & self.visit(tree.condition)

    def visit_print(self, tree):
        return self.visit(tree.expr)

    def visit_read(self, tree):
        return True

    def visit_function_call(self, tree):
        if tree.args:
            res = all([self.visit(x) for x in tree.args])
            return res & self.visit(tree.expr)
        else:
            return self.visit(tree.expr)

    def visit_reference(self, tree):
        return True

    def visit_binary_operation(self, tree):
        return self.visit(tree.lhs) & self.visit(tree.rhs)

    def visit_unary_operation(self, tree):
        return self.visit(tree.expr)
