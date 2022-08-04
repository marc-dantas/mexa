# MExA util file
from .expr import *


def n(value: Union[int, float]) -> Number:
    return Number(value)


def v(name: str, value: Union[int, float] = None) -> Variable:
    return Variable(name, value)


def op(op_type: str,
       first: OperationArgument,
       second: OperationArgument,
       *, highlight: bool = False) -> Operation:
    return Operation(op_type, first, second, highlight=highlight)


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
