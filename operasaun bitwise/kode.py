# AND bit-a-bit
print(5 & 3)  # Sai 1 (101 & 011 = 001)
print(format(5 & 3, '08b'))

# OR bit-a-bit
print(5 | 3)  # Sai 7 (101 | 011 = 111)
print(format(5 | 3, '08b'))
# XOR bit-a-bit
print(5 ^ 3)  # Sai 6 (101 ^ 011 = 110)
print(format(5 ^ 3, '08b'))
# NOT bit-a-bit
print(~5)     # Sai -6 (~101 = -110)
print(format(~5, '08b'))
# Shift left
print(5 << 1) # Sai 10 (101 << 1 = 1010)
print(format(5 << 1, '08b'))
# Shift right
print(5 >> 1) # Sai 2 (101 >> 1 = 10)
print(format(5 >> 1, '08b'))