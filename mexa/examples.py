from mexa.util import *

print("MExA Examples:")
print("Mass–energy equivalence")
print(eq(v('E'), mul(v('m'), squared(v('c')))))

print("Pythagorean Theorem")
print(eq(squared(v('a')), add(squared(v('b')), squared(v('c')))))

print("Random equation")
print(eq(mul(n(2), squared(v('x'))), add(v('x'), n(2))))

print("CLASSIC!")
print(eq(f('f', v('x')), add(v('x'), n(1))))