code = b'\x09\x04\x04\x09\x00\x00\x08\x01\x00\x08\x02\x01\x08\x03\x02\x06\x01\x04\x05\x01\x15\x07\x00\x01\x04\x00\x03\x01\x6B\xCC\x7E\x1D\x08\x01\x03\x04\x00\x01\x02\x0A\x04\x00\x09\x00\x00\x08\x01\x00\x08\x02\x01\x08\x03\x02\x06\x03\x08\x05\x03\x03\x07\x00\x03\x03\x00\x02\x01\x7C\x79\x79\x60\x08\x01\x03\x04\x00\x01\x02\x0A\x04\x00\x09\x00\x00\x08\x01\x00\x08\x02\x01\x08\x03\x02\x06\x01\x08\x07\x00\x01\x03\x00\x02\x01\xBD\xBD\xBC\x5F\x08\x01\x03\x04\x00\x01\x02\x0A\x04\x00\x00'
eip = 0
#num1 num2 num3
print('push num1')
print('push num2')
print('push num3')
while(True):
    if code[eip] == 0:# ret
        print('ret')                              
        break
    elif code[eip] == 1:#push dw_imm 5
        print("push %x"%int.from_bytes(code[eip+1:eip+5],'little'))
        eip+=5   
    elif code[eip] == 2:#pop(esp--)
        # print("esp--")
        eip+=1                         
    elif code[eip] == 3:#add reg,reg
        print("add r%x,r%x"%(code[eip+1],code[eip+2]))
        eip+=3
    elif code[eip] == 4:#sub reg,reg
        print("sub r%x,r%x"%(code[eip+1],code[eip+2]))
        eip+=3
    elif code[eip] == 5:#mul reg,imm
        print("mul r%x,0x%x"%(code[eip+1],code[eip+2]))
        eip+=3
    elif code[eip] == 6:#shr reg,imm
        print("shr r%x,0x%x"%(code[eip+1],code[eip+2]))
        eip+=3
    elif code[eip] == 7:#mov reg,reg
        print("mov r%x,r%x"%(code[eip+1],code[eip+2]))
        eip+=3
    elif code[eip] == 8:#mov reg,ss[imm]
        print("mov r%x,ss[%x]"%(code[eip+1],code[eip+2]))
        # print("pop r%x"%(code[eip+1]))
        eip+=3
    elif code[eip] == 9:#xor reg,reg
        print("xor r%x,r%x"%(code[eip+1],code[eip+2]))
        eip+=3
    elif code[eip] == 0xA:#or reg,reg
        print("or r%x,r%x"%(code[eip+1],code[eip+2]))
        eip+=3
    else:
        print('error')
        exit(-1)

print('--------------')
print('check:')
print('r4 || (unsigned __int8)num1 != 0x5E || (num2 & 0xFF0000) != 0x5E0000 || (unsigned __int8)num3 != 0x5E')


print('get three numbers')
from z3 import *
x1 = BitVec('x1',32)
x2 = BitVec('x2',32)
x3 = BitVec('x3',32)
solver = Solver()
solver.add(((x1>>4)*0x15) - x3 - 0x1d7ecc6b == 0)
solver.add(((x3>>8)*0x3) + x2 - 0x6079797c == 0)
solver.add(((x1>>8)+x2) - 0x5fbcbdbd == 0)
solver.add(x1 & 0xff == 0x5E)
solver.add(x2 & 0xFF0000 == 0x5E0000)
solver.add(x3 & 0xff == 0x5E)
solver.check()
print(solver.model())