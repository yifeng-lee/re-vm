
dest = [0x21, 0x58, 0x33, 0x57, 0x24, 0x2c, 0x66, 0x25,
        0x45, 0x53, 0x34, 0x28, 0x08, 0x61, 0x11, 0x07,
        0x14, 0x3d, 0x07, 0x62, 0x13, 0x72, 0x02, 0x4c]

flag = ""
random = 2019
for i in range(24):
    random = (random * 23333 + 19260817) % 127
    flag += chr(random ^ dest[i])

print(flag)