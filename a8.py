a =int(input("輸入五位數:"))
b = a//10000
c = a//1000 - b*10
d = a//100 - (b*100 + c*10)
e = a//10 - (b*1000 + c*100 + d*10)
f = a%10
print('結果:')
print(b)
print(c)
print(d)
print(e)
print(f)