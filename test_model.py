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


class TestBinaryOperation:
    def test_binary_operation_addition(self):
        assert 25 == get_v(BinaryOperation(Number(42), '+',
                                           Number(-17)))

    def test_binary_operation_multiplication(self):
        assert -51 == get_v(BinaryOperation(Number(3), '*',
                                            Number(-17)))

    def test_binary_operation_division(self):
        assert 14 == get_v(BinaryOperation(Number(42), '/',
                                           Number(3)))

    def test_binary_operation_module(self):
        assert 2 == get_v(BinaryOperation(Number(17), '%',
                                          Number(3)))

    def test_binary_operation_comparation(self):
        assert 0 != get_v(BinaryOperation(Number(42), '!=',
                                          Number(3)))

    def test_binary_operation_and(self):
        assert 0 == get_v(BinaryOperation(Number(0), '&&',
                                          Number(3)))

    def test_binary_operation_or(self):
        assert 0 != get_v(BinaryOperation(Number(0), '||',
                                          Number(42)))


class TestUnaryOperation:
    def test_unary_operation_minus(self):
        assert -42 == get_v(UnaryOperation('-', Number(42)))

    def test_unary_operation_not(self):
        assert 0 == get_v(UnaryOperation('!', Number(42)))
