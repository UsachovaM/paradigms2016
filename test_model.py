import pytest
import sys
import io
from io import StringIO
from model import *


def get_v(n):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    Print(n).evaluate(Scope())
    res = int(sys.stdout.getvalue())
    sys.stdout = old_stdout
    return res


class TestScope:
    def test_scope(self):
        scope = Scope()
        ans = 42
        scope["quest"] = ans
        assert scope["quest"] is ans

    def test_scope_parent(self):
        parent = Scope()
        scope = Scope(parent)
        ans = 42
        parent["quest"] = ans
        assert scope["quest"] is ans


class TestNumber:
    def test_number(self):
        assert get_v(Number(42)) == 42


class TestFunctionDefinition:
    def test_function_definition(self):
        scope = {}
        f = Function((), [Number(42)])
        fdef = FunctionDefinition('f', f)
        assert f is fdef.evaluate(scope)


class TestFunctionCall:
    def test_function_call(self):
        scope = {}
        scope["answer"] = Function((), [Number(42)])
        ans = FunctionCall(FunctionDefinition('func', scope["answer"]), [])
        assert get_v(ans) == 42


class TestReference:
    def test_reference(self):
        scope = {}
        ans = Function((), [Number(42)])
        scope["answer"] = ans
        assert Reference("answer").evaluate(scope) is ans


class TestFunction:
    def test_function(self):
        scope = {}
        Function((), []).evaluate(scope)


class TestConditional:
    def test_conditional(self):
        scope = {}
        Conditional(Number(1), [], []).evaluate(scope)
        Conditional(Number(0), None, None).evaluate(scope)
        Conditional(Number(1), None, [Number(1)]).evaluate(scope)
        Conditional(Number(0), [Number(1)], None).evaluate(scope)
        Conditional(Number(0), [Number(1)], []).evaluate(scope)
        Conditional(Number(0), [], [Number(1)]).evaluate(scope)


class TestRead:
    def test_read(self, monkeypatch):
        monkeypatch.setattr(sys, 'stdin', io.StringIO('6'))
        assert get_v(Read('a')) == 6


class TestPrint:
    def test_print(self, monkeypatch):
        monkeypatch.setattr(sys, 'stdout', io.StringIO())
        scope = {}
        Print(Number(42)).evaluate(scope)
        assert int(sys.stdout.getvalue()) == 42


class BinaryOperation:
    def test_binary_operation_addition():
        parent = Scope()
        assert 25 == BinaryOperation(Number(42), '+',
                                     Number(-17)).evaluate(parent).value

    def test_binary_operation_multiplication():
        parent = Scope()
        assert -51 == BinaryOperation(Number(3), '*',
                                      Number(-17)).evaluate(parent).value

    def test_binary_operation_division():
        parent = Scope()
        assert 14 == BinaryOperation(Number(42), '/',
                                     Number(3)).evaluate(parent).value

    def test_binary_operation_module():
        parent = Scope()
        assert 2 == BinaryOperation(UnaryOperation('-', Number(-17)), '%',
                                    Number(3)).evaluate(parent).value

    def test_binary_operation_comparation():
        parent = Scope()
        assert 0 != BinaryOperation(Number(42), '!=',
                                    Number(3)).evaluate(parent).value

    def test_binary_operation_and():
        parent = Scope()
        assert 0 == BinaryOperation(Number(0), '&&',
                                    Number(3)).evaluate(parent).value

    def test_binary_operation_or():
        parent = Scope()
        assert 0 != BinaryOperation(Number(0), '||',
                                    Number(42)).evaluate(parent).value


class UnaryOperation:
    def test_unary_operation_minus():
        parent = Scope()
        assert -42 == UnaryOperation('-', Number(42)).evaluate(parent).value

    def test_unary_operation_not():
        parent = Scope()
        assert 0 == UnaryOperation('!', Number(42)).evaluate(parent).value
