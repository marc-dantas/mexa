# MExA util file
from .expr import *


def n(value: Union[int, float]) -> Number:
    return Number(value)


def v(name: str) -> Variable:
    return Variable(name)


def op(op_type: str,
       first: OperationArgument,
       second: OperationArgument) -> Operation:
    return Operation(op_type, first, second)


def eq(first: OperationArgument, second: OperationArgument) -> Equation:
    return Equation(first, second)


def ine(ine_type: str, first: OperationArgument, second: OperationArgument) -> Inequality:
    return Inequality(ine_type, first, second)


def mul(x: OperationArgument, y: OperationArgument) -> Operation:
    return Operation(MULTIPLY, x, y)


def add(x: OperationArgument, y: OperationArgument) -> Operation:
    return Operation(SUM, x, y)


def sub(x: OperationArgument, y: OperationArgument) -> Operation:
    return Operation(SUBTRACT, x, y)


def div(x: OperationArgument, y: OperationArgument) -> Operation:
    return Operation(DIVIDE, x, y)


def squared(x: OperationArgument) -> Operation:
    return Operation(POWER, x, n(2))


def pow(x: OperationArgument, y: OperationArgument) -> Operation:
    return Operation(POWER, x, y)


def sqrt(x: OperationArgument) -> Operation:
    return Operation(ROOT, n(2), x)


def ine_ne(x: OperationArgument, y: OperationArgument) -> Inequality:
    return Inequality(NOT_EQ, x, y)


def ine_gt(x: OperationArgument, y: OperationArgument) -> Inequality:
    return Inequality(GREATER_THAN, x, y)


def ine_lt(x: OperationArgument, y: OperationArgument) -> Inequality:
    return Inequality(LESS_THAN, x, y)


def ine_ge(x: OperationArgument, y: OperationArgument) -> Inequality:
    return Inequality(GREATER_EQ, x, y)


def ine_le(x: OperationArgument, y: OperationArgument) -> Inequality:
    return Inequality(LESS_EQ, x, y)


def ine_ae(x: OperationArgument, y: OperationArgument) -> Inequality:
    return Inequality(ALMOST_EQ, x, y)