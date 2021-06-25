# -- Golf --

def AND(a,b):return 1 if a+b>1 else 0
def OR(a,b):return 1 if a+b>0 else 0
def XOR(a,b):return 1 if 2>a+b>0 else 0
def NOT(a):return ~-a
def NAND(a,b):return 0 if a+b>1 else 1
def NOR(a,b):return 0 if a+b>0 else 1
def XNOR(a,b):return 0 if 2>a+b>0 else 1

# -- Tests --

print('\nAND:')
print(AND(0,0)) # 0
print(AND(0,1)) # 0
print(AND(1,0)) # 0
print(AND(1,1)) # 1

print('\nOR:')
print(OR(0,0)) # 0
print(OR(0,1)) # 1
print(OR(1,0)) # 1
print(OR(1,1)) # 1

print('\nXOR:')
print(XOR(0,0)) # 0
print(XOR(0,1)) # 1
print(XOR(1,0)) # 1
print(XOR(1,1)) # 0

print('\nNOT:')
print(NOT(0)) # -1
print(NOT(1)) # 0

print('\nNAND:')
print(NAND(0,0)) # 1
print(NAND(0,1)) # 1
print(NAND(1,0)) # 1
print(NAND(1,1)) # 0

print('\nNOR:')
print(NOR(0,0)) # 1
print(NOR(0,1)) # 0
print(NOR(1,0)) # 0
print(NOR(1,1)) # 0

print('\nXNOR:')
print(XNOR(0,0)) # 1
print(XNOR(0,1)) # 0
print(XNOR(1,0)) # 0
print(XNOR(1,1)) # 1