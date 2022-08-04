# MExA expression file
from typing import Union

OperationArgument = Union['Number', 'Variable', 'Operation']
SUM = '+'
SUBTRACT = '-'
MULTIPLY = '∙'
DIVIDE = '÷'
POWER = '^'
ROOT = '√'
NOT_EQ = '≠'
GREATER_THAN = '>'
LESS_THAN = '<'
GREATER_EQ = '≥'
LESS_EQ = '≤'
ALMOST_EQ = '≈'

class Number:

    def __init__(self, value: Union[int, float]) -> None:
        self.__value = value

    @property
    def value(self) -> Union[int, float]:
        return self.__value

    @value.setter
    def value(self, x: Union[int, float]) -> None:
        self.__value = x

    def __repr__(self) -> str:
        return f'mexa.expr.Number({self.value})'

    def __str__(self) -> str:
        return str(self.value)


class Variable:

    def __init__(self, name: str, value: Union[int, float] = None) -> None:
        if len(name) > 1:
            raise NameError('A variable name can be only one character.')
        self.__name = name
        self.__value = value

    @property
    def value(self) -> Union[int, float]:
        return self.__value

    @property
    def name(self) -> str:
        return self.__name

    @value.setter
    def value(self, x: Union[int, float]) -> None:
        self.__value = x

    def __repr__(self) -> str:
        return f'mexa.expr.Variable({self.name!r})'

    def __str__(self) -> str:
        return self.name


class Operation:

    def __init__(self, op_type: str,
                 first: OperationArgument,
                 second: OperationArgument) -> None:
        if op_type not in (SUM, SUBTRACT, MULTIPLY, DIVIDE, POWER, ROOT):
            raise TypeError(f'Invalid operation type {op_type!r}.')
        self.__type = op_type
        self.__first = first
        self.__second = second

    @property
    def op_type(self) -> str:
        return self.__type

    @property
    def first(self) -> OperationArgument:
        return self.__first

    @property
    def second(self) -> OperationArgument:
        return self.__second

    def __process_literal(self) -> str:
        if formatted := self.__format():
            return formatted
        return f'{str(self.first)} {self.op_type} {str(self.second)}'

    def __format(self) -> str:
        if self.op_type == MULTIPLY:
            if isinstance(self.second, Variable):
                return f'{self.first}{self.second}'
        elif self.op_type == POWER:
            if isinstance(self.second, Number):
                if self.second.value == 2:
                    return f'{self.first}²'
                elif self.second.value == 3:
                    return f'{self.first}³'
            return f'{self.first}{self.op_type}{self.second}'
        elif self.op_type == ROOT:
            if isinstance(self.first, Number) and self.first.value == 2:
                return f'{self.op_type}{self.second}'
            return f'{self.first}{self.op_type}{self.second}'

    def __repr__(self) -> str:
        return f'mexa.expr.Operation(' \
               f'{repr(self.first)}, ' \
               f'{self.op_type!r}, ' \
               f'{repr(self.second)})'

    def __str__(self) -> str:
        return self.__process_literal()


class Equation:
    def __init__(self, first: OperationArgument, second: OperationArgument) -> None:
        self.__first = first
        self.__second = second

    @property
    def first(self) -> OperationArgument:
        return self.__first

    @property
    def second(self) -> OperationArgument:
        return self.__second

    def __repr__(self) -> str:
        return f'mexa.expr.Equation({repr(self.first)}, {repr(self.second)})'

    def __process_literal(self) -> str:
        return f'{str(self.first)} = {str(self.second)}'

    def __str__(self) -> str:
        return self.__process_literal()


class Inequality:

    def __init__(self, ine_type: str,
                 first: OperationArgument,
                 second: OperationArgument) -> None:
        if ine_type not in (NOT_EQ, GREATER_THAN,
                            LESS_THAN, GREATER_EQ,
                            LESS_EQ, ALMOST_EQ):
            raise TypeError(f'Invalid inequality type {ine_type!r}.')
        self.__type = ine_type
        self.__first = first
        self.__second = second

    @property
    def ine_type(self) -> str:
        return self.__type

    @property
    def first(self) -> OperationArgument:
        return self.__first

    @property
    def second(self) -> OperationArgument:
        return self.__second

    def __repr__(self) -> str:
        return f'mexa.expr.Inequality({repr(self.first)}, {self.__type!r}, {repr(self.second)})'

    def __process_literal(self) -> str:
        return f'{str(self.first)} {self.__type} {str(self.second)}'

    def __str__(self) -> str:
        return self.__process_literal()
