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
        ans = FunctionCall(FunctionDefinition('func', scope["answer"]),[])
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

def test_BinaryOperation():
    parent = Scope()
    x = Number(42)
    y = Number(-17)
    z = Number(3)
    p = Number(0)
    assert 25 == BinaryOperation(x, '+', y).evaluate(parent).value
    assert 59 == BinaryOperation(x, '-', y).evaluate(parent).value
    assert -51 == BinaryOperation(z, '*', y).evaluate(parent).value
    assert 14 == BinaryOperation(x, '/', z).evaluate(parent).value
    assert 2 == BinaryOperation(x, '/',
                                UnaryOperation('-', y)).evaluate(parent).value
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


def test_UnaryOperation():
    parent = Scope()
    x = Number(42)
    assert -42 == UnaryOperation('-', x).evaluate(parent).value
    assert 0 == UnaryOperation('!', x).evaluate(parent).value
