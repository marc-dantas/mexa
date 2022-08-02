from mexa.util import *

print("MExA Examples:")
print("Mass–energy equivalence")
print(
    equ(
        var('E'),
        op(
            MULTIPLY,
            var('m'),
            op(POWER, var('c'), num(2))
        )
    )
)

print("Pythagorean Theorem")
print(
    equ(
        op(POWER, var('a'), num(2)),
        op(
            SUM,
            op(POWER, var('b'), num(2)),
            op(POWER, var('c'), num(2))
        )
    )
)

