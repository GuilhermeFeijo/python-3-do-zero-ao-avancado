# conversão de tipos, coerção
# type converting, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1+2) # 3
print('1' + '2') # '12'
#print('1' + 1) # TypeError: can only concatenate str (not "int") to str

print(int('1'), type(int('1')+1)) # 1 <class 'int'>
print(int('1') + 1) # 2

print(3.0 + 1) # 4.0

print(bool('')) # False
print(bool(' ')) # True

print(str(11) + 'b') # '11b'