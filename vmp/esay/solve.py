code = [
    0x00000001, 0x00000065, 0x00000000, 0x00000001, 0x00000066, 0x000000DC,
    0x00000002, 0x00000065, 0x00000066, 0x00000001, 0x00000000, 0x00000065,
    0x00000001, 0x00000065, 0x00000001, 0x00000003, 0x00000065, 0x00000000,
    0x00000001, 0x00000001, 0x00000065, 0x00000001, 0x00000066, 0x00000001,
    0x00000001, 0x00000065, 0x00000002, 0x00000002, 0x00000065, 0x00000066,
    0x00000005, 0x00000065, 0x00000005, 0x00000065, 0x00000001, 0x00000002,
    0x00000065, 0x00000002, 0x00000003, 0x00000000, 0x00000002, 0x00000003,
    0x00000002, 0x00000005, 0x00000004, 0x00000004, 0x00000004, 0x000000D7,
    0x00000001, 0x00000066, 0x00000005, 0x00000001, 0x00000065, 0x000000E6,
    0x00000004, 0x00000066, 0x00000065, 0x00000001, 0x00000005, 0x00000066,
    0x00000006, 0x00000006, 0x00000006, 0x00000006, 0x00000001, 0x00000065,
    0x00000000, 0x00000002, 0x00000007, 0x00000065, 0x00000003, 0x00000008,
    0x000000E6, 0x00000004, 0x00000009, 0x000000D2, 0x00000001, 0x00000065,
    0x0000000A, 0x00000001, 0x00000066, 0x00000009, 0x00000003, 0x00000065,
    0x00000066, 0x00000001, 0x0000000A, 0x00000065, 0x00000006, 0x0000000B,
    0x00000005, 0x0000000B, 0x00000006, 0x0000000C, 0x00000003, 0x0000000C,
    0x0000000C, 0x00000001, 0x00000065, 0x0000000D, 0x00000001, 0x00000066,
    0x0000000E, 0x00000003, 0x00000066, 0x00000065, 0x00000001, 0x0000000E,
    0x00000066, 0x00000003, 0x00000065, 0x00000066, 0x00000001, 0x0000000D,
    0x00000065, 0x00000001, 0x00000065, 0x0000000F, 0x00000001, 0x00000066,
    0x00000010, 0x00000003, 0x00000066, 0x00000065, 0x00000001, 0x00000010,
    0x00000066, 0x00000004, 0x00000066, 0x00000065, 0x00000001, 0x0000000F,
    0x00000066, 0x00000006, 0x00000011, 0x00000006, 0x00000011, 0x00000004,
    0x00000012, 0x000000F0, 0x00000004, 0x00000012, 0x000000F0, 0x000000FF
]


def vm(opcode):
    eip = 0
    while True:
        if opcode[eip] == 1:
            if opcode[eip+2] < 0xC7:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('mov r%x,r%x'%(opcode[eip+1]-100,opcode[eip+2]-100))
                    else:
                        print('mov r%x,ds[%x]'%(opcode[eip+1]-100,opcode[eip+2]))
                else:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('mov ds[%x],r%x'%(opcode[eip+1],opcode[eip+2]-100))
                    else:
                        print('mov ds[%x],ds[%x]'%(opcode[eip+1],opcode[eip+2]))
            else:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    print('add r%x,0x%x'%(opcode[eip+1]-100,opcode[eip+2]+56))
                else:
                    print('mov ds[%x],0x%x'%(opcode[eip+1],opcode[eip+2]+56))
            eip+=3
        elif opcode[eip] == 2:
            if opcode[eip+2] < 0xC7:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('xor r%x,r%x'%(opcode[eip+1]-100,opcode[eip+2]-100))
                    else:
                        print('xor r%x,ds[%x]'%(opcode[eip+1]-100,opcode[eip+2]))
                else:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('xor ds[%x],r%x'%(opcode[eip+1],opcode[eip+2]-100))
                    else:
                        print('xor ds[%x],ds[%x]'%(opcode[eip+1],opcode[eip+2]))
            else:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    print('xor r%x,0x%x'%(opcode[eip+1]-100,opcode[eip+2]+56))
                else:
                    print('xor ds[%x],0x%x'%(opcode[eip+1],opcode[eip+2]+56))
            eip+=3
        elif opcode[eip] == 3:
            if opcode[eip+2] < 0xC7:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('add r%x,r%x'%(opcode[eip+1]-100,opcode[eip+2]-100))
                    else:
                        print('add r%x,ds[%x]'%(opcode[eip+1]-100,opcode[eip+2]))
                else:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('add ds[%x],r%x'%(opcode[eip+1],opcode[eip+2]-100))
                    else:
                        print('add ds[%x],ds[%x]'%(opcode[eip+1],opcode[eip+2]))
            else:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    print('add r%x,0x%x'%(opcode[eip+1]-100,opcode[eip+2]+56))
                else:
                    print('add ds[%x],0x%x'%(opcode[eip+1],opcode[eip+2]+56))
            eip+=3
        elif opcode[eip] == 4:
            if opcode[eip+2] < 0xC7:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('sub r%x,r%x'%(opcode[eip+1]-100,opcode[eip+2]-100))
                    else:
                        print('sub r%x,ds[%x]'%(opcode[eip+1]-100,opcode[eip+2]))
                else:
                    if opcode[eip+2] == 101 or opcode[eip+2] == 102:
                        print('sub ds[%x],r%x'%(opcode[eip+1],opcode[eip+2]-100))
                    else:
                        print('sub ds[%x],ds[%x]'%(opcode[eip+1],opcode[eip+2]))
            else:
                if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                    print('sub r%x,0x%x'%(opcode[eip+1]-100,opcode[eip+2]+56))
                else:
                    print('sub ds[%x],0x%x'%(opcode[eip+1],opcode[eip+2]+56))
            eip+=3
        elif opcode[eip] == 5:
            if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                print('inc r%x'%(opcode[eip+1]-100))
            else:
                print('inc ds[%x]'%(opcode[eip+1]))
            eip+=2
        elif opcode[eip] == 6:
            if opcode[eip+1] == 101 or opcode[eip+1] == 102:
                print('dec r%x'%(opcode[eip+1]-100))
            else:
                print('dec ds[%x]'%(opcode[eip+1]))
            eip+=2
        else:
            print('ret')
            return

vm(code)


dest = [0x72, 0xDE, 0xC1, 0xD4, 0x6D, 0x58, 0x6B, 0x2D, 0x87, 0x69, 0xC8, 0x6E, 0xDC, 0x47, 0xD3, 0x61, 0xC6, 0x71, 0x29, 0x7D]
dest[0x12] = (dest[0x12] + 0x128*2)&0xff 
dest[0x11] += 2
dest[0x10],dest[0x0f] = dest[0x0f],dest[0x10] - dest[0x0f]
for i in range(0x80):
    for j in range(0x80):
        if (i+j)&0xff == dest[0xe] and (i+j+i)&0xff == dest[0xd]:
            dest[0xd],dest[0xe] = i,j
dest[0xc] = (dest[0xc]//2)+1
dest[0xa] = (dest[0xa] -dest[0x9])&0xff
dest[9] = (dest[9]+0x10a)&0xff
dest[8] = (dest[8]-0x11e)&0xff
dest[7] ^= dest[0]
dest[6] += 2
tmp = dest[0]
dest[0] = (dest[0] ^ 0x114)&0xff
tmp1 = dest[1]
dest[1] = (dest[1] - tmp)&0xff
tmp2 = dest[2]
dest[2] = (dest[2] - 2) ^ tmp1
tmp3 = dest[3]
dest[3] ^= tmp2 ^ tmp
dest[4] = (dest[4]+0x10f-1)&0xff
dest[5] = (dest[5]+0x11e)&0xff


print(''.join(list(map(chr,dest))))