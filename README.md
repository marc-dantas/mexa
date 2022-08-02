# MExA
Math EXpression Abstraction

> WARNING! MExA is in development, it may have bugs and malfunctions 

## What is MExA?
MExA is a Python package made
to create abstractions for algebraic
expressions, with a dynamic interaction
between its members and even simple
evaluation.

## Getting Started
### Usage (Not working yet!)
#### Module `expr.py`
```py
class Number:
    value: int
    def __init__(self, value: int) -> None: ...;
    def __repr__(self) -> int: ...;
    def __str__(self) -> str: ...;

class OperationType(Enum):
    SUM = '+'
    SUBTRACT = '-'
    MULTIPLY = '×'
    DIVIDE = '÷'
    POWER = '^'
    ROOT = '√'

class Operation:
    op_type: OperationType
    first: Union[Number, Variable, Operation]
    second: Union[Number, Variable, Operation]
    def __init__(self, ...) -> None: ...;
    def process_literal(self) -> str: ...;
    def __repr__(self) -> tuple: ...;
    def __str__(self) -> str: ...;
    
class Variable:
    value: str
    def __init__(self, value: str) -> None: ...;
    def __repr__(self) -> str: ...;
    def __str__(self) -> str: ...;

class Equation:
    first: Operation
    second: Operation
    def __init__(self, ...) -> None: ...;
    def process_literal(self) -> str: ...;
    def __repr__(self) -> str: ...;
    def __str__(self) -> str: ...;
```
#### Module `util.py`
```py
def equ(...) -> Equation;
def num(...) -> Number;
def var(...) -> Variable;
def op(...) -> Operation;
SUM = OperationType.SUM
SUB = OperationType.SUBTRACT
MUL = OperationType.MULTIPLY
DIV = OperationType.DIVIDE
POW = OperationType.POWER
ROOT = OperationType.ROOT
```

> By marc-dantas