from z3 import *

enc = [
    0xF3, 0x2E, 0x18, 0x36, 0xE1, 0x4C, 0x22, 0xD1, 0xF9, 0x8C, 0x40, 0x76,
    0xF4, 0x0E, 0x00, 0x05, 0xA3, 0x90, 0x0E, 0xA5
]
x = [BitVec('x%s' % i, 8) for i in range(21)]
s = Solver()
for i in range(20):
    s.add(x[i]>>7 == 0)  
    s.add(((x[i + 1] + (x[i] % 7)) ^ ((x[i] ^ 18) * 3 + 2)) & 0xff == enc[i])

s.check()
res = [s.model().eval(x[i]).as_long() for i in range(21)]
print(''.join(list(map(chr,res))))
