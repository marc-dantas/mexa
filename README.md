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
# Symbol constants
SUM = '+'
SUBTRACT = '-'
MULTIPLY = '×'
DIVIDE = '÷'
POWER = '^'
ROOT = '√'

class Number:
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
    first: Operation
    second: Operation
    def __init__(self, ...) -> None: ...;
    def __repr__(self) -> str: ...;
    # Call this function to get the formatted string
    def __str__(self) -> str: ...;
```
#### Module `util.py`
```py
def equ(...) -> Equation;
def num(...) -> Number;
def var(...) -> Variable;
def op(...) -> Operation;
```
> Tip: Import the module `examples.py` and see some examples.

> By marc-dantas