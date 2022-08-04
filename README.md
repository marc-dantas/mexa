# MExA
Math EXpression Abstraction

> WARNING! MExA is in development, it may have bugs and malfunctions 
> Python version: 3.8+

## What is MExA?
MExA is a Python package made
to create abstractions for algebraic
expressions, with a dynamic interaction
between its members and even simple
evaluation.

## Getting Started
### Usage
#### Module `expr.py`
```py
# <Operation> operator constants
SUM = '+'
SUBTRACT = '-'
MULTIPLY = '×'
DIVIDE = '÷'
POWER = '^'
ROOT = '√'
# <Inequality> operator constants
NOT_EQ = '≠'
GREATER_THAN = '>'
LESS_THAN = '<'
GREATER_EQ = '≥'
LESS_EQ = '≤'
ALMOST_EQ = '≈'

class Number:
    # The number itself
    value: int
    def __init__(self, value: int) -> None: ...;
    def __repr__(self) -> int: ...;
    # Call this function to get the formatted string
    def __str__(self) -> str: ...;

class Variable:
    # Name of the variable (e.g. 'x', 'y', 'a', ...)
    name: str
    # Value of the variable
    value: Union[int, float] = None
    def __init__(self, ...) -> None: ...;
    def __repr__(self) -> str: ...;
    # Call this function to get the formatted string
    def __str__(self) -> str: ...;

class Operation:
    # The operation symbol
    op_type: str
    # First value
    first: Union[Number, Variable, Operation]
    # Second value
    second: Union[Number, Variable, Operation]
    def __init__(self, ...) -> None: ...;
    def __repr__(self) -> tuple: ...;
    # Call this function to get the formatted string
    def __str__(self) -> str: ...;

class Equation:
    # First operation/variable/number
    first: Union[Number, Variable, Operation]
    # Second operation/variable/number
    second: Union[Number, Variable, Operation]
    def __init__(self, ...) -> None: ...;
    def __repr__(self) -> str: ...;
    # Call this function to get the formatted string
    def __str__(self) -> str: ...;

class Inequality:
    # The inequality operator
    ine_type: str
    # First operation/variable/number
    first: Union[Number, Variable, Operation]
    # Second operation/variable/number
    second: Union[Number, Variable, Operation]
    def __init__(self, ...) -> None: ...;
    def __repr__(self) -> str: ...;
    # Call this function to get the formatted string
    def __str__(self) -> str: ...;
```
#### Module `util.py`
```py
# Class shortcuts
def eq(...)      -> Equation;
def ine(...)     -> Inequality;
def n(...)       -> Number;
def v(...)       -> Variable;
def op(...)      -> Operation;
# Operation shortcuts
def add(...)     -> Operation;
def sub(...)     -> Operation;
def mul(...)     -> Operation;
def div(...)     -> Operation;
def pow(...)     -> Operation;
def squared(...) -> Operation;
def sqrt(...)    -> Operation;
```
> Tip: Import the module `examples.py` and see some examples.

> By marc-dantas