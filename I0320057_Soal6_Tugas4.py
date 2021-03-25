x = 4       # 4 = 0000 0100
y = 11      # 11= 0000 1011
z = 0
print('==Operator Bitwise==')

print('\nx = 4')
print('y = 11')

z = x | y;     # 15 = 0000 1111
print('\nb. 4 | 11 =')
print('4  =', format(x,'08b'))
print('11 =', format(y,'08b'))
print('--------------(|)')
print(z,' =', format(z, '08b'))

z = x >> y;    # 0 = 0000 0000
print('\nb. 4 >> 11 =')
print('4  =', format(x,'08b'))
print('11 =', format(y,'08b'))
print('--------------(>>)')
print(z,' =', format(z, '08b'))

z = x ^ y;     # 15 = 0000 1111
print('\nb. 4 ^ 11 =')
print('4  =', format(x,'08b'))
print('11 =', format(y,'08b'))
print('--------------(^)')
print(z,'=', format(z, '08b'))

z = ~x;        # -5 = 1111 1011
print('\nb. ~4 =')
print('4  =', format(x,'08b'))
print('--------------(~)')
print(z,'=', format(z, '08b'))

z = x & y;      # 0 = 0000 0000
print('\nb. 4 & 11 =')
print('4  =', format(x,'08b'))
print('11 =', format(y,'08b'))
print('--------------(&)')
print(z,' =', format(z, '08b'))