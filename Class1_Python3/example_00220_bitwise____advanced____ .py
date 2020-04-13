# 0000 0001   = 1
# 0000 0011   = 3

print(1 & 3)  # = 1
print('{0:08b}'.format(1))
print('{0:08b}'.format(3))
print('{0:08b}'.format(1 & 3))
print()
print(1 | 3)  # = 3
print('{0:08b}'.format(1))
print('{0:08b}'.format(3))
print('{0:08b}'.format(1 | 3))
print()

# 0000 0001   = 1
# 0000 0011   = 3

# 0000 0001   = 1&3
# 0000 0011   = 1|3

print(1 | 2)  # = 3
print('{0:08b}'.format(1))
print('{0:08b}'.format(2))
print('{0:08b}'.format(1 | 2))
# 0000 0001   = 1
# 0000 0010   = 2
# 0000 0011   = 3

# 1:  0000 0001
print(1 << 2)  # 4 :  0000 0100
print('{0:08b}'.format(1))
print('{0:08b}'.format(1 << 2))
print()
print(3 << 2)
print('{0:08b}'.format(3 << 2))

print()
print(bin(3))
print()
print(hex(4))
print(hex(10))
