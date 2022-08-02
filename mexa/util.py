# MExA util file
from .expr import *


def num(value: Union[int, float]) -> Number:
    return Number(value)


def var(name: str, value: Union[int, float] = None) -> Variable:
    return Variable(name, value)


def op(op_type: str,
       first: OperationArgument,
       second: OperationArgument,
       *, highlight: bool = False) -> Operation:
    return Operation(op_type, first, second, highlight=highlight)


def equ(first: OperationArgument, second: OperationArgument) -> Equation:
    return Equation(first, second)
